import allure


@allure.feature("Управление списками Trello")
class TestTrelloLists:

    @allure.story("Получение списка всех колонок доски")
    def test_get_all_lists_on_board(self, api_client, test_board):
        board_id = test_board["id"]

        # Создаем 2 кастомных списка
        list_names = ["In Progress", "Code Review"]
        for name in list_names:
            res = api_client.create_list(board_id, name)
            assert res.status_code == 200, f"Ошибка создания списка '{name}': {res.text}"

        # Запрашиваем списки с доски
        response = api_client.get_board_lists(board_id)
        assert response.status_code == 200, f"Ошибка получения списков: {response.text}"

        lists_data = response.json()
        retrieved_names = [lst["name"] for lst in lists_data]

        for name in list_names:
            assert name in retrieved_names, f"Список '{name}' не найден среди {retrieved_names}"

    @allure.story("Архивация списка")
    def test_archive_list(self, api_client, test_board):
        board_id = test_board["id"]

        # 1. Создаем список
        list_res = api_client.create_list(board_id, "List to Archive")
        assert list_res.status_code == 200, f"Ошибка создания списка: {list_res.text}"
        list_id = list_res.json()["id"]

        # 2. Архивируем список
        archive_res = api_client.archive_list(list_id)
        assert archive_res.status_code == 200, f"Ошибка архивации списка: {archive_res.text}"
        assert archive_res.json()["closed"] is True
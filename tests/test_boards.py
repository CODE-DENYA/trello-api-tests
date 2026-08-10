import allure


@allure.feature("Управление объектами Trello")
class TestTrelloWorkflow:

    @allure.story("Сквозной сценарий: Работа со списками и карточками")
    def test_full_trello_workflow(self, api_client, test_board):
        board_id = test_board["id"]

        # 1. Создание списка
        list_res = api_client.create_list(board_id, "To Do")
        assert list_res.status_code == 200, f"Ошибка создания списка: {list_res.text}"
        list_id = list_res.json()["id"]

        # 2. Создание карточки в списке
        card_res = api_client.create_card(list_id, "Task #1: Run Tests")
        assert card_res.status_code == 200, f"Ошибка создания карточки: {card_res.text}"
        card_id = card_res.json()["id"]

        # 3. Проверка существования карточки
        get_card_res = api_client.get_card(card_id)
        assert get_card_res.status_code == 200, f"Ошибка получения карточки: {get_card_res.text}"
        assert get_card_res.json()["name"] == "Task #1: Run Tests"
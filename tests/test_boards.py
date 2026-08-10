import allure


@allure.feature("Управление досками Trello")
class TestBoards:

    @allure.story("Создание, получение и удаление доски")
    def test_board_lifecycle(self, api_client):
        board_name = "Test Automation Board"

        # 1. Создание доски
        create_res = api_client.create_board(board_name)
        assert create_res.status_code == 200, f"Ошибка создания: {create_res.text}"
        
        board_data = create_res.json()
        board_id = board_data["id"]
        assert board_data["name"] == board_name

        # 2. Получение информации о созданной доске
        get_res = api_client.get_board(board_id)
        assert get_res.status_code == 200, f"Ошибка получения: {get_res.text}"
        assert get_res.json()["id"] == board_id

        # 3. Удаление доски (очистка за собой)
        delete_res = api_client.delete_board(board_id)
        assert delete_res.status_code == 200, f"Ошибка удаления: {delete_res.text}"
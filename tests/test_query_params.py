import allure


@allure.feature("Query параметры и Фильтрация")
@allure.story("Проверка фильтрации возвращаемых полей (fields)")
class TestQueryParams:

    @allure.title("Запрос доски с фильтром fields возвращает только запрашиваемые поля")
    def test_get_board_with_fields_filter(self, api_client, test_board):
        params = {"fields": "name,url"}
        response = api_client.get_board(test_board["id"], params=params)
        assert response.status_code == 200

        board_data = response.json()

        # Проверяем наличие запрошенных полей (id Trello отдает всегда)
        assert "name" in board_data
        assert "url" in board_data
        assert "id" in board_data

        # Проверяем отсутствие полей, которые не запрашивались
        assert "closed" not in board_data
        assert "desc" not in board_data
        assert "idOrganization" not in board_data
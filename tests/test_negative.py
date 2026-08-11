import allure


@allure.feature("Негативные проверки Trello API")
class TestTrelloNegative:

    @allure.story("Запрос несуществующей доски")
    def test_get_non_existent_board(self, api_client):
        fake_board_id = "600000000000000000000000"
        response = api_client.get_board(fake_board_id)
        assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"

    @allure.story("Создание доски без авторизации")
    def test_create_board_without_auth(self, api_client):
        response = api_client.create_board(name="Unauthorized Board", use_auth=False)
        assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"

    @allure.story("Создание доски без обязательного параметра name")
    def test_create_board_without_name(self, api_client):
        response = api_client.create_board(name=None)
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"

    @allure.story("Запрос с невалидными учётными данными")
    def test_request_with_invalid_credentials(self, api_client):
        invalid_params = {"key": "invalid_key_123", "token": "invalid_token_123"}
        response = api_client.get_member(params=invalid_params, use_auth=False)
        assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
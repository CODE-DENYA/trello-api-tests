import allure
import requests
from config.config import Config


@allure.feature("Негативные проверки Trello API")
class TestTrelloNegative:

    @allure.story("Запрос несуществующей доски")
    def test_get_non_existent_board(self, api_client):
        fake_board_id = "600000000000000000000000"
        response = api_client.get_board(fake_board_id)
        assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"

    @allure.story("Создание доски без авторизации")
    def test_create_board_without_auth(self):
        url = f"{Config.BASE_URL}/boards"
        response = requests.post(url, params={"name": "Unauthorized Board"})
        assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"

    @allure.story("Создание доски без обязательного параметра name")
    def test_create_board_without_name(self):
        url = f"{Config.BASE_URL}/boards"
        # Передаем авторизацию, но не передаем параметр 'name'
        response = requests.post(url, params=Config.AUTH_PARAMS)
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"

    @allure.story("Запрос с невалидными учётными данными")
    def test_request_with_invalid_credentials(self):
        url = f"{Config.BASE_URL}/members/me"
        invalid_params = {"key": "invalid_api_key_12345", "token": "invalid_token_12345"}
        response = requests.get(url, params=invalid_params)
        assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
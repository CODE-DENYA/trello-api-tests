import allure
import requests
from config.config import Config


@allure.feature("Негативные проверки Trello API")
class TestTrelloNegative:

    @allure.story("Запрос несуществующей доски")
    def test_get_non_existent_board(self, api_client):
        fake_board_id = "600000000000000000000000"
        response = api_client.get_board(fake_board_id)

        # Сервер должен вернуть 404 Not Found
        assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"

    @allure.story("Создание доски без авторизации")
    def test_create_board_without_auth(self):
        # Попытка создать доску без API-ключа и токена
        url = f"{Config.BASE_URL}/boards"
        response = requests.post(url, params={"name": "Unauthorized Board"})

        # Trello возвращает 401 Unauthorized при попытке записи без ключа/токена
        assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
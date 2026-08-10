import allure
from jsonschema import validate
from schemas.board_schema import BOARD_SCHEMA


@allure.feature("Схемное тестирование (Contract Testing)")
class TestTrelloSchema:

    @allure.story("Валидация структуры JSON-ответа доски")
    def test_board_schema_validation(self, api_client, test_board):
        board_id = test_board["id"]
        response = api_client.get_board(board_id)
        assert response.status_code == 200, f"Ошибка получения доски: {response.text}"

        # Если структура ответа не совпадет со схемой, jsonschema выбросит ValidationError
        validate(instance=response.json(), schema=BOARD_SCHEMA)
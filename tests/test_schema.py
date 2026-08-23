import allure
from jsonschema import validate
from schemas.board_schema import BOARD_SCHEMA
from schemas.card_schema import CARD_SCHEMA
from schemas.list_schema import LIST_SCHEMA


@allure.feature("Схемное тестирование (Contract Testing)")
class TestTrelloSchema:

    @allure.story("Валидация структуры JSON-ответа доски")
    def test_board_schema_validation(self, api_client, test_board):
        board_id = test_board["id"]
        response = api_client.get_board(board_id)
        assert response.status_code == 200, f"Ошибка получения доски: {response.text}"

        validate(instance=response.json(), schema=BOARD_SCHEMA)

    @allure.story("Валидация структуры JSON-ответа списка и карточки")
    def test_list_and_card_schema_validation(self, api_client, test_board):
        board_id = test_board["id"]

        # Валидация списка
        list_res = api_client.create_list(board_id, "Schema Test List")
        assert list_res.status_code == 200, f"Ошибка создания списка: {list_res.text}"
        list_data = list_res.json()
        validate(instance=list_data, schema=LIST_SCHEMA)

        # Валидация карточки
        card_res = api_client.create_card(list_data["id"], "Schema Test Card")
        assert card_res.status_code == 200, f"Ошибка создания карточки: {card_res.text}"
        validate(instance=card_res.json(), schema=CARD_SCHEMA)
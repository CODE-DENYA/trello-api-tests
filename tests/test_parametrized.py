import allure
import pytest


@allure.feature("Параметризованные проверки Trello API")
class TestTrelloParametrized:

    @pytest.mark.parametrize(
        "board_name",
        [
            "Simple Board Name",
            "Тестовая доска на кириллице",
            "Board with symbols !@#$%^&*()",
            "Emoji Board 🚀🔥🎯",
            "A" * 100,  # Граничные значения: длинное имя из 100 символов
        ],
        ids=["english", "cyrillic", "symbols", "emoji", "long_name"],
    )
    @allure.story("Создание досок с различными валидными названиями")
    def test_create_board_with_different_names(self, api_client, board_name):
        # 1. Создаем доску
        response = api_client.create_board(board_name)
        assert response.status_code == 200, f"Ошибка создания доски '{board_name}': {response.text}"

        board_data = response.json()
        board_id = board_data["id"]

        try:
            # 2. Проверяем, что сервер сохранил имя корректно
            assert board_data["name"] == board_name
        finally:
            # 3. Гарантированно удаляем тестовую доску за собой
            api_client.delete_board(board_id)
import pytest
from api.trello_api import TrelloAPI


@pytest.fixture
def api_client():
    return TrelloAPI()


@pytest.fixture
def test_board(api_client):
    # Setup: создание доски перед запуском теста
    board_res = api_client.create_board("Fixture Test Board")
    assert board_res.status_code == 200, f"Ошибка создания доски в фикстуре: {board_res.text}"
    board_data = board_res.json()

    yield board_data  # Передаем данные созданной доски в тест

    # Teardown: автоматическое удаление доски после выполнения теста
    api_client.delete_board(board_data["id"])
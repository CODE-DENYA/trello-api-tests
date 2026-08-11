import uuid
import pytest
from api.trello_api import TrelloAPI


@pytest.fixture
def api_client():
    return TrelloAPI()


@pytest.fixture
def test_board(api_client):
    # Setup: генерация уникального имени и создание доски перед тестом
    unique_name = f"Test_Board_{uuid.uuid4().hex[:6]}"
    board_res = api_client.create_board(unique_name)
    assert board_res.status_code == 200, f"Ошибка создания доски в фикстуре: {board_res.text}"
    board_data = board_res.json()

    yield board_data  # Передаем данные созданной доски в тест

    # Teardown: безопасное автоматическое удаление доски после теста
    try:
        api_client.delete_board(board_data["id"])
    except Exception:
        pass
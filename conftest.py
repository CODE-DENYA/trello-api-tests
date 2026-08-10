import pytest
from api.trello_api import TrelloAPI


@pytest.fixture
def api_client():
    """Фикстура для инициализации API клиента Trello"""
    return TrelloAPI()
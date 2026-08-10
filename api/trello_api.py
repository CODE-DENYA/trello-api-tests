import requests
from config.config import Config


class TrelloAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.auth_params = Config.AUTH_PARAMS

    def create_board(self, name: str):
        """Создание новой доски в Trello"""
        url = f"{self.base_url}/boards"
        params = {**self.auth_params, "name": name}
        return requests.post(url, params=params)

    def get_board(self, board_id: str):
        """Получение информации о доске"""
        url = f"{self.base_url}/boards/{board_id}"
        return requests.get(url, params=self.auth_params)

    def delete_board(self, board_id: str):
        """Удаление доски"""
        url = f"{self.base_url}/boards/{board_id}"
        return requests.delete(url, params=self.auth_params)
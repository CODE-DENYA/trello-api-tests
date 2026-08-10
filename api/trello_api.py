import requests
from config.config import Config


class TrelloAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.auth_params = Config.AUTH_PARAMS

    # --- ДОСКИ (BOARDS) ---
    def create_board(self, name: str):
        """Создание новой доски"""
        url = f"{self.base_url}/boards"
        params = {**self.auth_params, "name": name}
        return requests.post(url, params=params)

    def get_board(self, board_id: str):
        """Получение информации о доске"""
        url = f"{self.base_url}/boards/{board_id}"
        return requests.get(url, params=self.auth_params)

    def update_board(self, board_id: str, **kwargs):
        """Обновление параметров доски (название, описание и т.д.)"""
        url = f"{self.base_url}/boards/{board_id}"
        params = {**self.auth_params, **kwargs}
        return requests.put(url, params=params)

    def delete_board(self, board_id: str):
        """Удаление доски"""
        url = f"{self.base_url}/boards/{board_id}"
        return requests.delete(url, params=self.auth_params)

    # --- СПИСКИ (LISTS) ---
    def create_list(self, board_id: str, name: str):
        """Создание списка на доске"""
        url = f"{self.base_url}/lists"
        params = {**self.auth_params, "name": name, "idBoard": board_id}
        return requests.post(url, params=params)

    def get_board_lists(self, board_id: str):
        """Получение всех списков на доске"""
        url = f"{self.base_url}/boards/{board_id}/lists"
        return requests.get(url, params=self.auth_params)

    def archive_list(self, list_id: str):
        """Архивация (закрытие) списка"""
        url = f"{self.base_url}/lists/{list_id}/closed"
        params = {**self.auth_params, "value": "true"}
        return requests.put(url, params=params)

    # --- КАРТОЧКИ (CARDS) ---
    def create_card(self, list_id: str, name: str):
        """Создание карточки в списке"""
        url = f"{self.base_url}/cards"
        params = {**self.auth_params, "name": name, "idList": list_id}
        return requests.post(url, params=params)

    def get_card(self, card_id: str):
        """Получение информации о карточке"""
        url = f"{self.base_url}/cards/{card_id}"
        return requests.get(url, params=self.auth_params)

    def update_card(self, card_id: str, **kwargs):
        """Обновление карточки (название, описание, перенос в другой список idList)"""
        url = f"{self.base_url}/cards/{card_id}"
        params = {**self.auth_params, **kwargs}
        return requests.put(url, params=params)
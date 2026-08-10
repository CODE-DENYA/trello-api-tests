import allure
import requests
from config.config import Config


class TrelloAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.auth_params = Config.AUTH_PARAMS

    # --- ДОСКИ (BOARDS) ---
    @allure.step("API: Создание доски '{name}'")
    def create_board(self, name: str):
        url = f"{self.base_url}/boards"
        params = {**self.auth_params, "name": name}
        return requests.post(url, params=params)

    @allure.step("API: Получение информации о доске ID '{board_id}'")
    def get_board(self, board_id: str):
        url = f"{self.base_url}/boards/{board_id}"
        return requests.get(url, params=self.auth_params)

    @allure.step("API: Обновление параметров доски ID '{board_id}'")
    def update_board(self, board_id: str, **kwargs):
        url = f"{self.base_url}/boards/{board_id}"
        params = {**self.auth_params, **kwargs}
        return requests.put(url, params=params)

    @allure.step("API: Удаление доски ID '{board_id}'")
    def delete_board(self, board_id: str):
        url = f"{self.base_url}/boards/{board_id}"
        return requests.delete(url, params=self.auth_params)

    # --- СПИСКИ (LISTS) ---
    @allure.step("API: Создание списка '{name}' на доске ID '{board_id}'")
    def create_list(self, board_id: str, name: str):
        url = f"{self.base_url}/lists"
        params = {**self.auth_params, "name": name, "idBoard": board_id}
        return requests.post(url, params=params)

    @allure.step("API: Получение списка всех колонок доски ID '{board_id}'")
    def get_board_lists(self, board_id: str):
        url = f"{self.base_url}/boards/{board_id}/lists"
        return requests.get(url, params=self.auth_params)

    @allure.step("API: Архивация списка ID '{list_id}'")
    def archive_list(self, list_id: str):
        url = f"{self.base_url}/lists/{list_id}/closed"
        params = {**self.auth_params, "value": "true"}
        return requests.put(url, params=params)

    # --- КАРТОЧКИ (CARDS) ---
    @allure.step("API: Создание карточки '{name}' в списке ID '{list_id}'")
    def create_card(self, list_id: str, name: str):
        url = f"{self.base_url}/cards"
        params = {**self.auth_params, "name": name, "idList": list_id}
        return requests.post(url, params=params)

    @allure.step("API: Получение карточки ID '{card_id}'")
    def get_card(self, card_id: str):
        url = f"{self.base_url}/cards/{card_id}"
        return requests.get(url, params=self.auth_params)

    @allure.step("API: Обновление карточки ID '{card_id}'")
    def update_card(self, card_id: str, **kwargs):
        url = f"{self.base_url}/cards/{card_id}"
        params = {**self.auth_params, **kwargs}
        return requests.put(url, params=params)
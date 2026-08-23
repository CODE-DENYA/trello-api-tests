import json
import allure
import requests
from config.config import Config


class TrelloAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.auth_params = Config.AUTH_PARAMS
        self.session = requests.Session()

    def _request(self, method: str, endpoint: str, params: dict | None = None, use_auth: bool = True):
        url = f"{self.base_url}{endpoint}"
        final_params = {}
        if use_auth:
            final_params.update(self.auth_params)
        if params:
            final_params.update(params)

        response = self.session.request(method, url, params=final_params, timeout=10)

        # Прикрепление деталей запроса и ответа в Allure
        allure.attach(
            f"URL: {response.url}\nMethod: {method}\nStatus: {response.status_code}",
            name="Request Details",
            attachment_type=allure.attachment_type.TEXT,
        )

        try:
            allure.attach(
                json.dumps(response.json(), indent=2, ensure_ascii=False),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON,
            )
        except Exception:
            allure.attach(
                response.text,
                name="Response Text",
                attachment_type=allure.attachment_type.TEXT,
            )

        return response

    # --- ДОСКИ (BOARDS) ---
    @allure.step("API: Создание доски '{name}'")
    def create_board(self, name: str | None = None, params: dict | None = None, use_auth: bool = True):
        request_params = {}
        if name is not None:
            request_params["name"] = name
        if params:
            request_params.update(params)
        return self._request("POST", "/boards", params=request_params, use_auth=use_auth)

    @allure.step("API: Получение информации о доске ID '{board_id}'")
    def get_board(self, board_id: str, params: dict | None = None, use_auth: bool = True):
        return self._request("GET", f"/boards/{board_id}", params=params, use_auth=use_auth)

    @allure.step("API: Обновление параметров доски ID '{board_id}'")
    def update_board(self, board_id: str, **kwargs):
        return self._request("PUT", f"/boards/{board_id}", params=kwargs)

    @allure.step("API: Удаление доски ID '{board_id}'")
    def delete_board(self, board_id: str, params: dict | None = None, use_auth: bool = True):
        return self._request("DELETE", f"/boards/{board_id}", params=params, use_auth=use_auth)

    # --- СПИСКИ (LISTS) ---
    @allure.step("API: Создание списка '{name}' на доске ID '{board_id}'")
    def create_list(self, board_id: str, name: str):
        params = {"name": name, "idBoard": board_id}
        return self._request("POST", "/lists", params=params)

    @allure.step("API: Получение списка всех колонок доски ID '{board_id}'")
    def get_board_lists(self, board_id: str):
        return self._request("GET", f"/boards/{board_id}/lists")

    @allure.step("API: Архивация списка ID '{list_id}'")
    def archive_list(self, list_id: str):
        params = {"value": "true"}
        return self._request("PUT", f"/lists/{list_id}/closed", params=params)

    # --- КАРТОЧКИ (CARDS) ---
    @allure.step("API: Создание карточки '{name}' в списке ID '{list_id}'")
    def create_card(self, list_id: str, name: str):
        params = {"name": name, "idList": list_id}
        return self._request("POST", "/cards", params=params)

    @allure.step("API: Получение карточки ID '{card_id}'")
    def get_card(self, card_id: str):
        return self._request("GET", f"/cards/{card_id}")

    @allure.step("API: Обновление карточки ID '{card_id}'")
    def update_card(self, card_id: str, **kwargs):
        return self._request("PUT", f"/cards/{card_id}", params=kwargs)

    # --- ПОЛЬЗОВАТЕЛИ (MEMBERS) ---
    @allure.step("API: Получение профиля пользователя")
    def get_member(self, member_id: str = "me", params: dict | None = None, use_auth: bool = True):
        return self._request("GET", f"/members/{member_id}", params=params, use_auth=use_auth)
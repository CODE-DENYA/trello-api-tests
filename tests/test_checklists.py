import allure


@allure.feature("Чек-листы")
@allure.story("Управление чек-листами в карточках")
class TestChecklists:

    @allure.title("Создание и чтение чек-листа в карточке")
    def test_create_and_get_checklist(self, api_client, test_board):
        # Setup: создаем колонку и карточку
        list_res = api_client.create_list(test_board["id"], "List for Checklist")
        assert list_res.status_code == 200
        list_id = list_res.json()["id"]

        card_res = api_client.create_card(list_id, "Card with Checklist")
        assert card_res.status_code == 200
        card_id = card_res.json()["id"]

        # Action 1: создание чек-листа
        checklist_name = "Definition of Done"
        create_res = api_client.create_checklist(card_id, checklist_name)
        assert create_res.status_code == 200
        checklist_data = create_res.json()

        assert checklist_data["name"] == checklist_name
        assert checklist_data["idCard"] == card_id

        # Action 2: получение и проверка чек-листа
        get_res = api_client.get_checklist(checklist_data["id"])
        assert get_res.status_code == 200
        assert get_res.json()["id"] == checklist_data["id"]
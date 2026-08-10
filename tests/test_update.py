import allure


@allure.feature("Обновление объектов Trello (PUT)")
class TestTrelloUpdate:

    @allure.story("Изменение названия и описания доски")
    def test_update_board_details(self, api_client, test_board):
        board_id = test_board["id"]
        new_name = "Обновленная Доска"
        new_desc = "Автоматическое описание доски"

        # 1. Отправляем PUT-запрос на изменение
        update_res = api_client.update_board(board_id, name=new_name, desc=new_desc)
        assert update_res.status_code == 200, f"Ошибка обновления доски: {update_res.text}"

        # 2. Проверяем обновленные данные через GET
        get_res = api_client.get_board(board_id)
        board_data = get_res.json()
        assert board_data["name"] == new_name
        assert board_data["desc"] == new_desc

    @allure.story("Перемещение карточки в другой список")
    def test_move_card_between_lists(self, api_client, test_board):
        board_id = test_board["id"]

        # 1. Создаем два списка: "To Do" и "Done"
        list_todo_id = api_client.create_list(board_id, "To Do").json()["id"]
        list_done_id = api_client.create_list(board_id, "Done").json()["id"]

        # 2. Создаем карточку в списке "To Do"
        card_id = api_client.create_card(list_todo_id, "Задача для переноса").json()["id"]

        # 3. Перемещаем карточку в список "Done" и меняем имя
        update_res = api_client.update_card(
            card_id, 
            idList=list_done_id, 
            name="Задача выполнена"
        )
        assert update_res.status_code == 200, f"Ошибка перемещения карточки: {update_res.text}"

        # 4. Проверяем, что idList и name действительно изменились
        card_data = api_client.get_card(card_id).json()
        assert card_data["idList"] == list_done_id
        assert card_data["name"] == "Задача выполнена"
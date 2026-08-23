import allure

MAX_RESPONSE_TIME_SECONDS = 2.0  # Допустимый лимит времени ответа API


@allure.feature("SLA и Производительность")
@allure.story("Проверка времени ответа ключевых эндпоинтов")
class TestAPIPerformanceSLA:

    @allure.title("SLA: Время ответа при получении профиля пользователя не превышает 2.0 с")
    def test_get_member_sla(self, api_client):
        response = api_client.get_member()
        assert response.status_code == 200

        elapsed_time = response.elapsed.total_seconds()
        allure.attach(
            f"Время ответа: {elapsed_time:.3f} сек",
            name="Performance Metric",
            attachment_type=allure.attachment_type.TEXT,
        )
        assert elapsed_time < MAX_RESPONSE_TIME_SECONDS, (
            f"SLA превышен! Запрос выполнялся {elapsed_time:.3f}s (лимит: {MAX_RESPONSE_TIME_SECONDS}s)"
        )

    @allure.title("SLA: Время ответа при чтении данных доски не превышает 2.0 с")
    def test_get_board_sla(self, api_client, test_board):
        response = api_client.get_board(test_board["id"])
        assert response.status_code == 200

        elapsed_time = response.elapsed.total_seconds()
        allure.attach(
            f"Время ответа: {elapsed_time:.3f} сек",
            name="Performance Metric",
            attachment_type=allure.attachment_type.TEXT,
        )
        assert elapsed_time < MAX_RESPONSE_TIME_SECONDS, (
            f"SLA превышен! Запрос выполнялся {elapsed_time:.3f}s (лимит: {MAX_RESPONSE_TIME_SECONDS}s)"
        )
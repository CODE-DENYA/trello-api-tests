# 🚀 Trello API Automated Testing Framework

Проект по автоматизации тестирования REST API сервиса [Trello](https://trello.com) с использованием **Python**, **Pytest**, **Requests** и **Allure**.

[![Trello API Tests](https://github.com/CODE-DENYA/trello-api-tests/actions/workflows/run-tests.yml/badge.svg)](https://github.com/CODE-DENYA/trello-api-tests/actions/workflows/run-tests.yml) [![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://code-denya.github.io/trello-api-tests/)

---

## 🛠 Технологический стек

* **Язык:** Python 3.12
* **Фреймворк тестирования:** Pytest
* **HTTP-клиент:** Requests (с сессиями Keep-Alive и таймаутами)
* **Валидация контрактов (JSON Schema):** jsonschema
* **Отчётность:** Allure Framework (детализация шагов, логирование запросов/ответов)
* **CI/CD:** GitHub Actions (регулярный прогон по расписанию) + GitHub Pages

---

## 🧪 Покрытие тестами

1. **CRUD операции над сущностями Trello (test_boards.py, test_lists.py, test_update.py):**
   * Создание, получение, обновление и удаление досок (Boards) и списков (Lists).
   * Перенос карточек между списками.
2. **Негативное тестирование (test_negative.py):**
   * Проверка ответов сервера при передаче невалидных токенов, несуществующих ID и некорректных параметров (400 Bad Request, 401 Unauthorized, 404 Not Found).
3. **Параметризованное тестирование (test_parametrized.py):**
   * Проверка обработки названий с кириллицей, эмодзи, спецсимволами и граничной длиной строк.
4. **Интеграционный E2E сценарий:**
   * Полный жизненный цикл: Создание доски -> Создание списка -> Создание карточки -> Чтение карточки.
5. **Контрактное тестирование (test_schema.py):**
   * Строгая проверка структуры и типов данных JSON-ответов сервера (Boards, Lists, Cards) с помощью JSON Schema.

---

## 📁 Структура проекта

    trello-api-tests/
    ├── .github/
    │   └── workflows/
    │       └── run-tests.yml     # CI/CD пайплайн для запуска тестов и деплоя отчёта
    ├── api/
    │   └── trello_api.py         # API-клиент (Session, Timeout, @allure.step, attachment)
    ├── config/
    │   └── config.py             # Загрузка и валидация конфигурации из .env
    ├── schemas/
    │   ├── board_schema.py       # JSON-схема структуры доски
    │   ├── card_schema.py        # JSON-схема структуры карточки
    │   └── list_schema.py        # JSON-схема структуры списка
    ├── tests/
    │   ├── test_boards.py        # Позитивный E2E тест
    │   ├── test_lists.py         # Тесты работы со списками
    │   ├── test_negative.py      # Негативные проверки
    │   ├── test_parametrized.py  # Граничные и параметризованные тесты
    │   ├── test_schema.py        # Тесты валидации JSON Schema
    │   └── test_update.py        # Тесты обновления сущностей
    ├── .env.example              # Шаблон переменных окружения
    ├── conftest.py               # Pytest-фикстуры (Setup/Teardown)
    ├── pytest.ini                # Конфигурация Pytest
    └── requirements.txt          # Зависимости проекта

---

## 🚀 Локальный запуск тестов

### 1. Клонирование репозитория
```bash
git clone https://github.com/CODE-DENYA/trello-api-tests.git
cd trello-api-tests
```

### 2. Установка зависимостей
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создай файл `.env` в корне проекта на основе `.env.example`:
```bash
cp .env.example .env
```
*(Для PowerShell в Windows: `Copy-Item .env.example .env`)*

Укажи свои ключи Trello API в файле `.env`:
```env
TRELLO_API_KEY=ваш_api_key
TRELLO_TOKEN=ваш_token
```

### 4. Запуск тестов и генерация отчёта
```bash
pytest
allure serve allure-results
```
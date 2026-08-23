# 🚀 Trello API — API Test Automation Framework

Проект по автоматизации тестирования REST API сервиса [Trello](https://trello.com/) с использованием **Python**, **Pytest**, **Requests** и **Allure**.

[![Trello API Tests](https://github.com/CODE-DENYA/trello-api-tests/actions/workflows/run-tests.yml/badge.svg)](https://github.com/CODE-DENYA/trello-api-tests/actions/workflows/run-tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://CODE-DENYA.github.io/trello-api-tests/)

---

## 🛠 Технологический стек

* **Язык программирования:** Python 3.12
* **Фреймворк тестирования:** Pytest
* **HTTP-клиент:** Requests (с сессиями Keep-Alive, таймаутами и автоматическим ретраем через `HTTPAdapter` и `Retry` для статусов 429, 500, 502, 503, 504)
* **Контрактное тестирование:** jsonschema (валидация JSON-схем ответов)
* **Конфигурация:** python-dotenv (безопасное управление переменными окружения из файла `.env`)
* **Качество кода:** Ruff (линтер)
* **Отчетность:** Allure Framework (`allure-pytest`) с детализированными шагами (`@allure.step`) и прикреплением запросов/ответов (`allure.attach`)
* **CI/CD:** GitHub Actions (автоматический прогон по пушам, pull request'ам и ночному расписанию в 3:00 UTC, линтинг и публикация Allure-отчета на GitHub Pages)

---

## 🧪 Покрытие тестами

Тестовый набор охватывает ключевые сценарии интеграционного, функционального и контрактного тестирования REST API Trello:

### 📋 Управление досками и списками (`tests/test_boards.py`, `tests/test_lists.py`, `tests/test_update.py`, `tests/test_checklists.py`)
* **Сквозной workflow:** Создание досок, списков (`To Do`) и карточек с валидацией их существования.
* **Управление списками:** Получение всех колонок доски и архивация списка с проверкой флага `closed: true`.
* **Обновление данных (PUT):** Изменение названия и описания досок, а также перенос карточек между списками (`idList`) с одновременным переименованием.
* **Чек-листы:** Создание и проверка элементов структуры чек-листов внутри карточек.

### 🚫 Негативное тестирование (`tests/test_negative.py`)
* **Несуществующие ресурсы:** Запрос несуществующей доски возвращает статус `404 Not Found`.
* **Безопасность и авторизация:** Попытка взаимодействия без авторизации или с невалидными учетными данными корректно отклоняется с кодом `401 Unauthorized`.
* **Валидация параметров:** Обработка запросов с пропущенными обязательными параметрами (`name=None`) с возвратом `400 Bad Request`.

### 🔠 Параметризованные тесты (`tests/test_parametrized.py`)
* **Граничные значения и кодировки:** Проверка создания досок с именами на кириллице, спецсимволами (`!@#$%^&*()`), эмодзи (`🚀🔥🎯`) и длинными строками (100 символов) с использованием `@pytest.mark.parametrize`.

### 📐 Контрактное тестирование (`tests/test_schema.py`)
* **Валидация JSON Schema:** Строгая проверка соответствия структур ответа сервера для досок (`BOARD_SCHEMA`), списков (`LIST_SCHEMA`) и карточек (`CARD_SCHEMA`) с помощью библиотеки `jsonschema`.

### 🔍 Фильтрация и Query-параметры (`tests/test_query_params.py`)
* **Проекция полей:** Проверка работы параметра `fields=name,url` — API возвращает только запрошенные поля и базовый `id`, исключая лишние данные.

### ⚡ SLA и Производительность (`tests/test_sla.py`)
* **Контроль времени отклика:** Замеры времени выполнения ключевых эндпоинтов (профиль пользователя, чтение доски) с жестким лимитом `< 2.0` секунд и фиксацией метрик в Allure.

---

## 🏗 Архитектурные особенности фреймворка

* **Централизованный API-клиент (`api/trello_api.py`):** Инкапсуляция всех эндпоинтов в класс `TrelloAPI`, автоматическая подстановка ключей авторизации и гибкая настройка сеансов `requests.Session`.
* **Автоматические ретраи:** Встроенный механизм `HTTPAdapter` с `Retry` для прозрачной обработки временных сетевых сбоев, таймаутов и ограничений rate limit.
* **Глубокая интеграция с Allure:** Каждый метод клиента фиксирует в отчете URL, HTTP-метод, статус-код, а также тело ответа в формате JSON или текста для быстрой дебаг-аналитики.
* **Управление тестовыми данными (`conftest.py`):** Фикстура `test_board` автоматически генерирует уникальное имя с помощью `uuid`, создает доску перед тестом и гарантированно удаляет её (Teardown) после выполнения даже в случае падения теста.

---

## 📁 Структура проекта

```text
trello-api-tests/
├── .github/
│   └── workflows/
│       └── run-tests.yml        # CI/CD пайплайн GitHub Actions
├── api/
│   └── trello_api.py            # API-клиент (Requests, ретраи, Allure-шаги)
├── config/
│   └── config.py                # Загрузка и валидация конфигурации из .env
├── schemas/
│   ├── board_schema.py          # JSON-схема структуры доски
│   ├── card_schema.py           # JSON-схема структуры карточки
│   └── list_schema.py           # JSON-схема структуры списка
├── tests/                       # Автотесты (Pytest)
│   ├── test_boards.py           # Позитивный E2E-сценарий работы с доской
│   ├── test_checklists.py       # Тесты управления чек-листами
│   ├── test_lists.py            # Тесты списков и архивации
│   ├── test_negative.py         # Негативные проверки (400, 401, 404)
│   ├── test_parametrized.py     # Параметризованные тесты названий
│   ├── test_query_params.py     # Проверка query-параметров и фильтрации
│   ├── test_schema.py           # Контрактное тестирование (JSON Schema)
│   ├── test_sla.py              # Проверка производительности и SLA
│   └── test_update.py           # Обновление сущностей и перемещение карточек
├── .env.example                 # Шаблон переменных окружения
├── .gitignore                   # Исключения Git
├── conftest.py                  # Pytest-фикстуры (создание и удаление досок)
├── pytest.ini                   # Конфигурация Pytest и Allure
├── requirements.txt             # Зависимости проекта
└── README.md                    # Документация проекта
```

---

## 🚀 Локальный запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/CODE-DENYA/trello-api-tests.git
cd trello-api-tests
```

### 2. Создание и активация виртуального окружения
```bash
python -m venv venv
```
* **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\activate
  ```
* **macOS / Linux / Git Bash:**
  ```bash
  source venv/bin/activate
  ```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создайте файл `.env` в корне проекта на основе шаблона `.env.example`:

* **macOS / Linux / Git Bash:**
  ```bash
  cp .env.example .env
  ```
* **Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```

Заполните ваши реальные ключи Trello API в файле `.env`:
```env
TRELLO_API_KEY=ваш_api_key_сюда
TRELLO_TOKEN=ваш_token_сюда
TRELLO_BASE_URL=https://api.trello.com/1
```

### 5. Запуск тестов
* **Запуск всех тестов:**
  ```bash
  pytest
  ```
* **Запуск с генерацией Allure-результатов:**
  ```bash
  pytest --alluredir=allure-results
  ```
* **Просмотр Allure-отчета локально:**
  ```bash
  allure serve allure-results
  ```
* **Проверка стиля и качества кода (Ruff):**
  ```bash
  ruff check .
  ```

---

## 🔄 CI/CD Пайплайн

При каждом push, pull request или по ночному расписанию (ежедневно в 3:00 UTC) в GitHub Actions запускается пайплайн:
1. Разворачивается чистая среда Ubuntu с установленным Python 3.12.
2. Устанавливаются зависимости проекта из `requirements.txt`.
3. Выполняется статическая проверка кода линтером **Ruff**.
4. Запускаются API-тесты с использованием секретов GitHub Actions (`TRELLO_API_KEY`, `TRELLO_TOKEN`).
5. Генерируется и публикуется актуальный HTML-отчет **Allure Report** на GitHub Pages.
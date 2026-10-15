
# Notes API Tests

Автоматизированное тестирование Notes App API на Python.

## Используемые технологии

- Python
- requests
- pytest
- ООП
- pytest fixtures

## Структура проекта

api/
- base_api.py - базовый класс для HTTP запросв
- auth_api.py - регистрация и авторизация
- notes_api.py - работа с заметками

tests/
- conftest.py - фикстуры pytest
- test_auth.py - тесты регистрации и авторизации
- test_get_notes.py - тесты GET
- test_post_notes.py - тесты POST
- test_delete_notes.py - тесты DELETE

## Реализованные API-методы

- POST /api/register
- POST /api/login
- GET /api/notes
- POST /api/notes
- DELETE /api/notes/{note_id}

## Установка зависимостей

pip install -r requirements.txt

## Запуск автотестов

Из папки notes_api:

python -m pytest tests/ -v

## Результаты тестирования

Всего реализовано 15 автотестов

- GET Notes: 3 PASSED
- POST Notes: 3 PASSED
- DELETE Notes: 4 PASSED
- Login: 2 PASSED
- Register: 2 PASSED, 1 FAILED

## Обнаруженное расхождение

При отправке POST /api/register без обязательного
поля password сервер возвращает 500 Internal Server Error.

Ожидаемый статус в тесте: 400 Bad Request.

Фактическая ошибка сервера:

KeyError: 'password'

Тест test_register_400 оставлен с ожидаемым
статусом 400 для фиксации расхождения.

## Особенности реализации

- API классы реализованы с использованием наследования.
- Авторизация выполняется с помощью JWT-токена.
- Тестовые данные создаются с уникальными значениями.
- Для подготовки тестов используются фикстуры pytest.
- Созданные тестовые заметки автоматически удаляются.

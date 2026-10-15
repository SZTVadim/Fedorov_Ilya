
from uuid import uuid4

import pytest


@pytest.fixture
def created_note(auth_token, notes_api):
    title = f"Тестовая заметка {uuid4().hex}"

    response = notes_api.create_note(
        token=auth_token,
        title=title,
        content="Проверка создания заметки"
    )

    yield response

    notes_response = notes_api.get_notes(auth_token)
    assert notes_response.status_code == 200

    for note in notes_response.json():
        if note["title"] == title:
            delete_response = notes_api.delete_note(
                auth_token,
                note["id"]
            )
            assert delete_response.status_code == 200


def test_create_note_201(created_note):
    assert created_note.status_code == 201
    assert created_note.json()["message"] == "Заметка создана!"


def test_create_note_401(notes_api):
    response = notes_api.create_note(
        token="",
        title="Тестовая заметка",
        content="Проверка без токена"
    )

    assert response.status_code == 401
    assert response.json()["message"] == "Token is missing!"


def test_create_note_403(notes_api):
    response = notes_api.create_note(
        token="invalid_token",
        title="Тестовая заметка",
        content="Проверка неверного токена"
    )

    assert response.status_code == 403
    assert response.json()["message"] == "Token is invalid or expired!"

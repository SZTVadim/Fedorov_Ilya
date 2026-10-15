
from uuid import uuid4

import pytest

from api.auth_api import AuthAPI


@pytest.fixture
def note_for_delete(auth_token, notes_api):
    title = f"Заметка для удаления {uuid4().hex}"

    response = notes_api.create_note(
        token=auth_token,
        title=title,
        content="Проверка DELETE"
    )

    assert response.status_code == 201

    response = notes_api.get_notes(auth_token)
    assert response.status_code == 200

    found_notes = [
        note for note in response.json()
        if note["title"] == title
    ]

    assert len(found_notes) == 1

    note_id = found_notes[0]["id"]

    yield note_id

    response = notes_api.get_notes(auth_token)
    assert response.status_code == 200

    for note in response.json():
        if note["id"] == note_id:
            delete_response = notes_api.delete_note(
                auth_token,
                note_id
            )
            assert delete_response.status_code == 200


def test_delete_note_200(auth_token, notes_api, note_for_delete):
    response = notes_api.delete_note(
        auth_token,
        note_for_delete
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Note deleted!"

    response = notes_api.get_notes(auth_token)

    assert response.status_code == 200
    assert all(
        note["id"] != note_for_delete
        for note in response.json()
    )


def test_delete_note_401(notes_api):
    response = notes_api.delete_note("", 1)

    assert response.status_code == 401
    assert response.json()["message"] == "Token is missing!"


def test_delete_note_403(notes_api):
    response = notes_api.delete_note("invalid_token", 1)

    assert response.status_code == 403
    assert response.json()["message"] == (
        "Token is invalid or expired!"
    )


def test_delete_note_409(auth_token, notes_api, note_for_delete):
    auth = AuthAPI()

    response = auth.login(
        email="ilya_aqa_20261015_002@example.com",
        password="Test123456"
    )

    assert response.status_code == 200

    token_2 = response.json()["token"]

    response = notes_api.delete_note(
        token_2,
        note_for_delete
    )

    assert response.status_code == 409
    assert response.json()["message"] == (
        "Not authorized to delete this note"
    )

    response = notes_api.get_notes(auth_token)

    assert response.status_code == 200
    assert any(
        note["id"] == note_for_delete
        for note in response.json()
    )

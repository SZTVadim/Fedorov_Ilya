
import pytest

from api.auth_api import AuthAPI
from api.notes_api import NotesAPI


@pytest.fixture
def auth_token():
    auth = AuthAPI()

    response = auth.login(
        email="ilya_aqa_20261015_001@example.com",
        password="Test123456"
    )

    assert response.status_code == 200

    return response.json()["token"]


@pytest.fixture
def notes_api():
    return NotesAPI()

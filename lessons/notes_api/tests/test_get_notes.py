
def test_get_notes_200(auth_token, notes_api):
    response = notes_api.get_notes(auth_token)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_notes_401(notes_api):
    response = notes_api.get_notes("")

    assert response.status_code == 401
    assert response.json()["message"] == "Token is missing!"


def test_get_notes_403(notes_api):
    response = notes_api.get_notes("invalid_token")

    assert response.status_code == 403
    assert response.json()["message"] == "Token is invalid or expired!"

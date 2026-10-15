
from uuid import uuid4

from api.auth_api import AuthAPI


def test_login_200():
    auth = AuthAPI()

    response = auth.login(
        email="ilya_aqa_20261015_001@example.com",
        password="Test123456"
    )

    assert response.status_code == 200
    assert "token" in response.json()
    assert isinstance(response.json()["token"], str)


def test_login_401():
    auth = AuthAPI()

    response = auth.login(
        email="ilya_aqa_20261015_001@example.com",
        password="wrong_password"
    )

    assert response.status_code == 401
    assert response.json()["message"] == (
        "Ошибка авторизации... Пожалуйста, проверь почту или пароль"
    )


def test_register_201():
    auth = AuthAPI()

    unique_id = uuid4().hex[:12]
    email = f"test_{unique_id}@example.com"
    username = f"user_{unique_id}"

    response = auth.register(
        email=email,
        password="Test123456",
        username=username
    )

    assert response.status_code == 201
    assert response.json()["message"] == "Успешная регистрация!"


def test_register_409():
    auth = AuthAPI()

    response = auth.register(
        email="ilya_aqa_20261015_001@example.com",
        password="Test123456",
        username="ilya_aqa"
    )

    assert response.status_code == 409
    assert response.json()["message"].strip() == (
        "Пользователь с таким email уже существует"
    )


def test_register_400():
    auth = AuthAPI()

    unique_id = uuid4().hex[:12]

    data = {
        "email": f"test_{unique_id}@example.com",
        "username": f"user_{unique_id}"
    }

    response = auth.post("/api/register", data=data)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 400

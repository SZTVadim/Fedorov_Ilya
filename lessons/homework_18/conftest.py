import pytest
import time


@pytest.fixture
def test_user():
    print("SETUP: создаём тестового пользователя")
    return "Test user"


@pytest.fixture
def delete_user():
    yield
    print("TEARDOWN: удаляем тестового пользователя")


@pytest.fixture
def test_timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Тест выполнялся: {end - start:.2f} сек")


@pytest.fixture
def setup_user(test_user, delete_user, test_timer):
    return test_user


@pytest.fixture
def base():
    print("SETUP base")
    yield
    print("TEARDOWN base")


@pytest.fixture
def auth(base):
    print("SETUP auth")
    yield
    print("TEARDOWN auth")


@pytest.fixture
def db():
    print("SETUP db")
    yield
    print("TEARDOWN db")


@pytest.fixture
def bundle(auth, db):
    print("SETUP bundle")
    yield
    print("TEARDOWN bundle")


@pytest.fixture
def cache():
    print("SETUP cache")
    yield
    print("TEARDOWN cache")


@pytest.fixture
def warm_cache(cache):
    print("SETUP warm_cache")
    yield
    print("TEARDOWN warm_cache")


@pytest.fixture
def logger(base, db):
    print("SETUP logger")
    yield
    print("TEARDOWN logger")


@pytest.fixture
def app(bundle):
    print("SETUP app")
    yield
    print("TEARDOWN app")


@pytest.fixture
def metrics():
    print("SETUP metrics")
    yield
    print("TEARDOWN metrics")

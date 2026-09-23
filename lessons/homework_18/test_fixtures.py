import time


def test_user_flow(setup_user):
    print(setup_user)
    time.sleep(3)


def test_puzzle(app, logger):
    print("TEST")

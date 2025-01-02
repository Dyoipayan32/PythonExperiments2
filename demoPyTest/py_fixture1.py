import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_fixture_auto_use():
    print("setting up")
    yield
    print("performing tear down")


@pytest.fixture()
def setup_fixture():
    print("setting up")
    yield
    print("performing tear down")


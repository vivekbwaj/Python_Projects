import pytest

@pytest.fixture(scope="module")
def mySetUp():
    print("I execute before each module only")

@pytest.fixture()
def myTearDown():
    print("I execute before each method")
    yield
    print("I execute after each method")
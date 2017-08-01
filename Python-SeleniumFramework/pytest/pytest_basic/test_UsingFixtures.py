import pytest

@pytest.fixture()
def mySetUp():
    print("I execute before each method")
    yield
    print("I execute after each method")

def test_py_1(mySetUp):
    print("This is test 1")
    assert False

def test_py_2(mySetUp):
    print("This is test 2")

    # py.test - v - s test_usingfixtures.py::test_py_1
    # to run a specific test only
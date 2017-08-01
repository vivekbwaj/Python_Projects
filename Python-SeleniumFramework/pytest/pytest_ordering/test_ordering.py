import pytest

@pytest.fixture()
def mySetUp():
    print("I execute before each method")

@pytest.mark.run(order=2)
def test_py_1(mySetUp):
    print("This is test 1")

@pytest.mark.run(order=3)
def test_py_2(mySetUp):
    print("This is test 2")

@pytest.mark.run(order=1)
def test_py_3(mySetUp):
    print("This is test 3")
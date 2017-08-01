import unittest
from selenium import webdriver
import os

class unittestSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("I will run only once before all tests")
        driverLocation = "E:\Python-SeleniumFramework\python_behave_Framework\dependencies"
        os.environ["webdriver.gecko.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        cls.driver = webdriver.Firefox(driverLocation)

    def test_Case_1(self):
        print("Running method A")
        self.driver.get("https://docs.pytest.org/en/latest/")

    def test_Case_2(self):
        print("Running method B")
        self.driver.get("https://docs.python.org/2/library/unittest.html")

    @classmethod
    def tearDownClass(cls):
        print("I will run only once after all tests")
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)

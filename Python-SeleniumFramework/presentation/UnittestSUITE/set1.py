import unittest
from termcolor import colored

class set1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before all methods for set 1")

    def setUp(self):
        print("This is setup method for set 1")

    def testCase_1(self):
        print("This is set 1 test case 1")

    def testCase_2(self):
        print("This is set 1 test case 2")

    def tearDown(self):
        print("This is teardown method for set 1")

    @classmethod
    def tearDownClass(cls):
        print("After all methods for set 1")
        print(colored("##########################",'white'))

if __name__ == '__main__':
    unittest.main(verbosity=1)

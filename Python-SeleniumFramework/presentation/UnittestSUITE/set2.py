import unittest
from termcolor import colored

class set2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before all methods for set 2")

    def setUp(self):
        print("This is setup method for set 2")

    def testSet2_Test1(self):
        print("This is set 2 test case 1")

    def testSet2_Test2(self):
        print("This is set 2 test case 2")

    def tearDown(self):
        print("This is teardown method for set 2")

    @classmethod
    def tearDownClass(cls):
        print("After all methods for set 2")
        print(colored("##########################", 'white'))

if __name__ == '__main__':
    unittest.main(verbosity=1)

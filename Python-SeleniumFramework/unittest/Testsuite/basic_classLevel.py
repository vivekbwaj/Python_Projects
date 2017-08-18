import unittest

class myClass_basic_2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Before all methods")

    def setUp(self):
        print("This is setup method")

    def testCase_1(self):
        print("This is test case 1")

    def testCase_2(self):
        print("This is test case 2")

    def tearDown(self):
        print("This is teardown method")

    @classmethod
    def tearDownClass(cls):
        print("After all methods")

if __name__ == '__main__':
    unittest.main(verbosity=1)

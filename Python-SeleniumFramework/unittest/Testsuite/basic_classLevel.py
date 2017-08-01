import unittest

class myClass_basic_2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is setup method before all methods")

    def testCase_1(self):
        print("This is test case 1")

    def testCase_2(self):
        print("This is test case 2")

    @classmethod
    def tearDownClass(cls):
        print("This is teardown method after all methods")


if __name__ == '__main__':
    unittest.main(verbosity=1)

import unittest

class myClass_basic_1(unittest.TestCase):

    def setUp(self):
        print("This is setup method")

    def testCase_1(self):
        print("This is test case 1 with Pass status ")

    def testCase_2(self):
        print("This is test case 2 with fail status")
        assert False

    def tearDown(self):
        print("This is teardown method")


if __name__ == '__main__':
    unittest.main(verbosity=0)

    #
    #
    # 0 (quiet): you just get the total numbers of tests executed and the global result
    # 1 (default): you get the same plus a dot for every successful test or a F for every failure
    # 2 (verbose): you get the help string of every test and the result
    #

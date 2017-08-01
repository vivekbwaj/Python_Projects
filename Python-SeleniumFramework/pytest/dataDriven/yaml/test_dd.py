import pytest,unittest
from ddt import ddt, unpack, data
from util import hello
from util import getValues
from util import getDt


@ddt
class Test_Class_1(unittest.TestCase):

    @data(getValues())
    def test_py_1(self,a):
        print(a)
        # print(getValues())
        # print(lang)

    @data(("Language"))
    def test_2(self, lang):
        print(getDt())
        hello(lang)
        print(getValues())
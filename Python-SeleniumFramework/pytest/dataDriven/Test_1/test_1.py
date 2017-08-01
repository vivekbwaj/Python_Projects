import pytest,unittest
from ddt import ddt, unpack, data


@ddt
class Test_Class_1(unittest.TestCase):

    @data(("Ruby","Cucumber"), ("Python","Behave"))
    @unpack
    def test_py_1(self, lang,fr):
        print(lang+" "+fr)

    @data(("Rspec"),("behave"))
    def test_2(self, lang):
        print(lang)
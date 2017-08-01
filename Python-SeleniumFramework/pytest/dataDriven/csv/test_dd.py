import pytest,unittest
from ddt import ddt, unpack, data
from readData import getCSVData


@ddt
class Test_Class_1(unittest.TestCase):

    @data(*getCSVData("E:\Python-SeleniumFramework\pytest\dataDriven\csv\\testdata.csv"))
    @unpack
    def test_py_1(self, a,b,c,d):
        print(a)

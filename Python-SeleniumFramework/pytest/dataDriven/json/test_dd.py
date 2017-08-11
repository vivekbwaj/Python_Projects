import pytest,unittest
from ddt import ddt, unpack, data
from readDataJ import getJSONData


@ddt
class Test_Class_1(unittest.TestCase):

    @data(*getJSONData("E:\Python-SeleniumFramework\pytest\dataDriven\json\\myjson.json"))
    # @unpack
    def test_py_1(self,a):
        for x in a:
            print(x)




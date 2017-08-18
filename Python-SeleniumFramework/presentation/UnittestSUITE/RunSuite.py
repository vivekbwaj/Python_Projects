import unittest
from set1 import set1
from set2 import set2

testSet1=unittest.TestLoader().loadTestsFromTestCase(set1)
testSet2=unittest.TestLoader().loadTestsFromTestCase(set2)

e2e=unittest.TestSuite([testSet1,testSet2])
smoke=unittest.TestSuite([testSet1])
sanity=unittest.TestSuite([testSet1])

unittest.TextTestRunner(verbosity=1).run(e2e)
# unittest.TextTestRunner(verbosity=1).run(smoke)
# unittest.TextTestRunner(verbosity=1).run(sanity)
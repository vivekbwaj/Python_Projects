import unittest
from basic_classLevel import myClass_basic_2
from basic_methodLevel import myClass_basic_1

clsLevel=unittest.TestLoader().loadTestsFromTestCase(myClass_basic_2)
metLevel=unittest.TestLoader().loadTestsFromTestCase(myClass_basic_1)

e2e=unittest.TestSuite([clsLevel,metLevel])
smoke=unittest.TestSuite([clsLevel])
sanity=unittest.TestSuite([metLevel])

unittest.TextTestRunner(verbosity=1).run(e2e)
# unittest.TextTestRunner(verbosity=1).run(smoke)
# unittest.TextTestRunner(verbosity=1).run(sanity)
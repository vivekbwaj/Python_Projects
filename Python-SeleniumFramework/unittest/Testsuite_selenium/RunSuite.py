import unittest
from BDD import BDD
from Emails import Emails
from Social import Social


# Get all tests from Emails, Social and BDD
ema = unittest.TestLoader().loadTestsFromTestCase(Emails)
soc = unittest.TestLoader().loadTestsFromTestCase(Social)
bdd = unittest.TestLoader().loadTestsFromTestCase(BDD)

# Create a test suite contained in Emails, Social and BDD
smokeTest = unittest.TestSuite([ema, soc])
sanityTest=unittest.TestSuite([bdd])

unittest.TextTestRunner(verbosity=1).run(sanityTest)
unittest.TextTestRunner(verbosity=1).run(smokeTest)
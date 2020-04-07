import unittest
from MyAccountPackage.test_Login import LoginTest
from MyAccountPackage.test_PersonalInformation import PersonalInfoTest
from ShoppingCart_Test.test_shoppingCartTestCase import ShoppingCart

# Get all test from all test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(PersonalInfoTest)

# Creating test suites
masterTestSuite = unittest.TestSuite()
masterTestSuite.addTest(tc1)
masterTestSuite.addTest(tc2)

# Run Test Suite
unittest.TextTestRunner().run(masterTestSuite)
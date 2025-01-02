# First of all import unittest
import unittest

from pythonTestAutomationTraining.unittest.utest_1_test import TestClass, TestClass2

# create new Test Suite
suite_1 = unittest.TestSuite()
suite_2 = unittest.TestSuite()
# convert Test Case to Test Suite
# add to existing Test Suite
suite_1.addTest(unittest.makeSuite(TestClass))
suite_2.addTest(unittest.makeSuite(TestClass2))
# suite_1.addTest(TestClass())
# suite_2.addTest(TestClass2())


# Combine suites into a single suite
combined_suites = unittest.TestSuite([suite_1, suite_2])

# Run the test suites
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(combined_suites)

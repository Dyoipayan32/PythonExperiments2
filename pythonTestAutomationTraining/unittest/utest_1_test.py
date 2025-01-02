# First of all import unittest
import unittest


# Create new Test Case to implement and group tests
class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # is executed once cest case starts.
        print('Test Case "TestClass" has started.')

    @classmethod
    def tearDownClass(cls):
        # is executed once Test Case finishes.
        print('Test Case "TestClass" has finished.')

    def setUp(self):
        # is executed before every test in Test Case.
        print('Check {} has started.'.format(self._testMethodName))

    def tearDown(self):
        # is executed after every test in Test Case.
        print('Check {} has finished.'.format(self._testMethodName))

    def test_true_method(self):
        # create our first test
        self.assertTrue(True)

    def test_assertion_fails_two_method(self):
        # create our fifth test
        self.assertTrue(False)


class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # is executed once cest case starts.
        print('Test Case "TestClass2" has started.')

    @classmethod
    def tearDownClass(cls):
        # is executed once Test Case finishes.
        print('Test Case "TestClass2" has finished.')

    def setUp(self):
        # is executed before every test in Test Case.
        print('Check {} has started.'.format(self._testMethodName))

    def tearDown(self):
        # is executed after every test in Test Case.
        print('Check {} has finished.'.format(self._testMethodName))

    def test_false_method(self):
        # create our second test
        self.assertFalse(False)

    def test_assertion_fails_one_method(self):
        # create our fourth test
        self.assertFalse(True)

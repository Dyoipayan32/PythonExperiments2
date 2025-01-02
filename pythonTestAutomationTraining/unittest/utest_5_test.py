# First of all import unittest
import unittest
from unittest import mock, TestCase


def not_implemented_method():
    print("Yet to be implemented")
    return "Yet to be implemented"


# Create a new Test Case to implement and group tests
class TestClass(TestCase):

    @mock.patch("utest_5_test.not_implemented_method")
    def test_not_implemented_method(self, result):
        # create a mock object as a substitution for the existing method
        # result is a variable that stores mocked method
        result.return_value = "Mocked Method"
        method_to_mock = not_implemented_method()
        self.assertEqual(method_to_mock, "Mocked Method")
        print(result.called)
        self.assertTrue(result.called)
        result.assert_called_once()

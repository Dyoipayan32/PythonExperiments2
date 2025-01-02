import unittest
from typing import Any
from math import sqrt
from math import pi


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        # is executed before every test in Test Case.
        self.calc = Calculator()
        self.calc.arg1 = 625
        self.calc.arg2 = 100
        print("first number as input : ", self.calc.arg1)
        print("second number as input : ", self.calc.arg2)
        print('Check {} has started.'.format(self._testMethodName))

    def tearDown(self):
        # is executed after every test in Test Case.
        print('Check {} has finished.'.format(self._testMethodName))

    def test_sum(self):
        """This test function validates sum of two numbers"""
        print("Value of sum: ", self.calc.get_sum())
        self.assertEqual(self.calc.get_sum(), 725)

    def test_multiply(self):
        """This test function validates multiplication of two numbers"""
        print("Value of multiplication: ", self.calc.get_multiplication())
        self.assertEqual(self.calc.get_multiplication(), 62500)

    def test_subtract(self):
        """This test function validates subtraction of two numbers"""
        print("Value of subtraction: ", self.calc.get_subtraction())
        self.assertEqual(self.calc.get_subtraction(), 525)

    def test_divide(self):
        """This test function validates division of two numbers"""
        print("Value of division: ", self.calc.get_division())
        self.assertEqual(self.calc.get_division(), 6.25)

    def test_sqrt(self):
        """This test function validates square root of given first number"""
        print("Value of square root: ", self.calc.get_sqrt())
        self.assertEqual(self.calc.get_sqrt(), 25)

    def test_pi(self):
        """This test function validates approximate value close to the value of pi
        till 2 decimal places."""
        print("Value of pi: ", self.calc.get_pi())
        self.assertAlmostEqual(self.calc.get_pi(), 3.142, 2)


class Calculator:
    def __int__(self, x, y):
        self.arg1 = x
        self.arg2 = y

    def get_sum(self) -> Any:
        """
        performs sum of two numbers
        :return: int: float:double
        """
        return self.arg1 + self.arg2

    def get_multiplication(self) -> Any:
        """
        performs multiplication. It multiplies value, arg1 with value, arg2  --> arg1 * arg2
        :return: int: float:double
        """
        return self.arg1 * self.arg2

    def get_subtraction(self) -> Any:
        """
        performs subtraction. It subtracts value, arg2 from value,  arg1 --> arg1 - arg2
        :return: int: float:double
        """
        return self.arg1 - self.arg2

    def get_division(self) -> Any:
        """
        performs division.
        Where arg1 is dividend and arg2 is divisor and the output is quotient --> arg1/arg2
        :return: int: float:double
        """
        return self.arg1 / self.arg2

    def get_sqrt(self) -> Any:
        """
        performs square root on given number.
        Where arg1 is taken the desired number as default to find the square root.--> sqrt(arg1)
        :return: int: float:double
        """
        return sqrt(self.arg1)

    @staticmethod
    def get_pi() -> Any:
        """
        return the value of pi.
        requires no argument as input.
        :return: float:double
        """
        return pi

from typing import Any
from math import sqrt
from math import pi


class Calculator:
    def __int__(self, x=None, y=None):
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

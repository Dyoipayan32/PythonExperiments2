import pytest


@pytest.mark.regression
def test_method1():
    print("Running test method1")


@pytest.mark.regression
def test_method2():
    print("Running test method2")


def test_method3():
    print("Running test method3")


def test_method4():
    print("Running test method4")

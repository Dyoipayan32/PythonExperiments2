import pytest


class TestFix01:

    def test_fix1(self):
        print("inside test method 1")
        a = 4 + 4
        assert a == 8

    def test_fix2(self):
        print("inside test method 2")
        a = 4 + 4
        assert a == 8

    @pytest.mark.xfail(reason="Expected to fail")
    def test_another_function(self):
        # Your test logic here
        assert False

    @pytest.mark.skip(reason="Expected to skip")
    def test_another_function2(self):
        # Your test logic here
        assert True

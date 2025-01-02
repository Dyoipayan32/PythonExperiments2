import sys
import pytest


class TestFix04:
    val = 4

    """
    The `capsys` built-in fixture can be used to capture output from `sys.stdout` and `sys.stderr`.
    """

    def test_example(self, capsys):
        # sys.stdout.write("Hello\n")
        print("Hello")
        captured = capsys.readouterr()
        print(captured.out+str(1))
        assert captured.out+str(1) == "Hello\n1"

    def test_raising_exception1(self):
        with pytest.raises(ValueError) as valErr_info:
            raise ValueError("This is a custom exception message")
        print(str(valErr_info.value))

    def test_raising_exception2(self):
        with pytest.raises(ZeroDivisionError) as except_info:
            var = 1 / 0
            print(var)
        print(str(except_info.value))

import pytest


class TestFix04:
    """
    Below test function is an example of using parametrize decorator
    """
    @pytest.mark.parametrize('test_input, expected', [("3+4", 7,), ("3+5", 8,), ("3+3", 6,)])
    def test_evaluate_compare(self, test_input, expected):
        assert eval(test_input) == expected

    """
        Below test function is an example of using parametrized fixture
    """
    def test_eval_inputs(self, evaluate_inputs):
        assert eval(evaluate_inputs[0]) == evaluate_inputs[1]


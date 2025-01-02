import pytest


class TestCollection:
    # Example tests
    @pytest.mark.custom_marker
    def test_example_one(self):
        assert True

    def test_example_two(self):
        assert True

    @pytest.mark.custom_marker
    def test_example_three(self):
        assert True
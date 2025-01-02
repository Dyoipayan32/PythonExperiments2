import pytest
import time


# Example test that will pass
def _fast():
    assert True


# Example test that will fail due to timeout
# @pytest.mark.timeout(2)  # Timeout set to 1 second
def _slow():
    time.sleep(1)
    assert True


# @pytest.mark.timeout(3)  # Timeout set to 5 seconds
def test_timeout_exceeded():
    # Simulate a long-running process
    time.sleep(3)  # This will cause the test to exceed the timeout and fail
    assert True  # This line will not be reached


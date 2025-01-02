import logging

# Creating a basic logger
logger = logging.getLogger(__name__)


def fun(n):
    logger.warning(msg="Example Warning")
    return n * 5


def test_sample():
    assert fun(2) == 10

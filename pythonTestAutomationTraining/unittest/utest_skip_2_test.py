import unittest


@unittest.skip("Whole TestCase class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

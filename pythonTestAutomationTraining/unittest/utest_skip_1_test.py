import unittest
import sys


class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        # Test should not be executed in any case
        # self.fail() - method that fails
        # test with text in brackets
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"),
                         "requires Windows")
    def test_windows_support(self):
        # Test should be skipped if OS is not Windows
        pass

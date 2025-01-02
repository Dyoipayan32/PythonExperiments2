'''
Expected Test Failures
Sometimes, tests should fail to show whether an application works correctly.
For example, if you write a test to check for the ability to log in with an incorrect login and password,
 it will fail, and such behavior will be correct.
 But how do you explain this to unittest?
 To do this, such tests should be decorated with

 @unittest.expectedFailure*.

'''

import unittest


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


'''
When a test is decorated like this, unittest will expect that test's correct behavior is to Fail . 
If it does, the test will be marked as Passed; otherwise, it will be marked as Failed.
'''
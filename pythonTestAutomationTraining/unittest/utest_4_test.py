# import module mock from unittest
from unittest import mock, TestCase

# create a new Mock object and assign it to the variable
m = mock.Mock()

print(m.called)
print(m.call_count)
print(m.call_args)
print(m.call_args_list)


def function_to_be_tested(function):
    # function that calls another function that was passed as an input argument
    function()
    print("I finished my work")


# New test case to create and group tests
class TestClass(TestCase):

    def test_function_behavior(self):
        # test checks if the mock object that was passed to the function
        # was called
        # mock_object = mock.Mock()
        function_to_be_tested(m)
        # Now check if mock_object was called during the function execution
        print(m.called)
        print(m.call_count)
        print(m.call_args)
        print(m.call_args_list)
        self.assertTrue(m.called)
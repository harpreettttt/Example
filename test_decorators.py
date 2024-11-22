# test_decorators.py

import unittest
from unittest.mock import patch
from decorators import time_logger
import time

class TestTimeLoggerDecorator(unittest.TestCase):
    def test_decorator_prints_execution_time(self):
        """
        Test that the time_logger decorator prints the correct execution time message.
        """
        @time_logger
        def sample_function():
            time.sleep(0.1)
            return "Done"

        with patch('builtins.print') as mocked_print:
            result = sample_function()
            self.assertEqual(result, "Done")
            mocked_print.assert_called_once()
            # Extract the print argument
            print_call_args = mocked_print.call_args[0][0]
            # Check the format of the print message
            self.assertTrue(print_call_args.startswith("Function 'sample_function' executed in "))
            self.assertTrue(print_call_args.endswith(" seconds."))

    def test_decorator_with_arguments(self):
        """
        Test that the decorator works with functions that take positional and keyword arguments.
        """
        @time_logger
        def multiply(a, b, delay=0):
            if delay > 0:
                time.sleep(delay)
            return a * b

        with patch('builtins.print') as mocked_print:
            result = multiply(3, 4, delay=0.2)
            self.assertEqual(result, 12)
            mocked_print.assert_called_once()
            print_call_args = mocked_print.call_args[0][0]
            self.assertTrue(print_call_args.startswith("Function 'multiply' executed in "))
            self.assertTrue(print_call_args.endswith(" seconds."))

    def test_decorator_preserves_return_value(self):
        """
        Ensure that the decorator does not alter the return value of the decorated function.
        """
        @time_logger
        def get_message():
            return "Hello, World!"

        with patch('builtins.print'):
            result = get_message()
            self.assertEqual(result, "Hello, World!")

    def test_decorator_preserves_function_name(self):
        """
        Ensure that the decorator preserves the original function's name.
        """
        @time_logger
        def original_function():
            return "Original"

        self.assertEqual(original_function.__name__, "original_function")

    def test_decorator_preserves_docstring(self):
        """
        Ensure that the decorator preserves the original function's docstring.
        """
        @time_logger
        def function_with_doc():
            """This is a test function."""
            return "Doc Test"

        self.assertEqual(function_with_doc.__doc__, "This is a test function.")


    def test_decorator_multiple_calls(self):
        """
        Test that the decorator works correctly when the decorated function is called multiple times.
        """
        @time_logger
        def increment(x):
            return x + 1

        with patch('builtins.print') as mocked_print:
            result1 = increment(1)
            result2 = increment(2)
            result3 = increment(3)
            self.assertEqual(result1, 2)
            self.assertEqual(result2, 3)
            self.assertEqual(result3, 4)
            self.assertEqual(mocked_print.call_count, 3)
            for i in range(1, 4):
                print_call_args = mocked_print.call_args_list[i-1][0][0]
                self.assertTrue(print_call_args.startswith("Function 'increment' executed in "))
                self.assertTrue(print_call_args.endswith(" seconds."))

    def test_decorator_non_sleeping_function(self):
        """
        Test the decorator with a function that does not have any delays.
        """
        @time_logger
        def add(a, b):
            return a + b

        with patch('builtins.print') as mocked_print:
            result = add(5, 7)
            self.assertEqual(result, 12)
            mocked_print.assert_called_once()
            print_call_args = mocked_print.call_args[0][0]
            self.assertTrue(print_call_args.startswith("Function 'add' executed in "))
            self.assertTrue(print_call_args.endswith(" seconds."))

if __name__ == '__main__':
    unittest.main()

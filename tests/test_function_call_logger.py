import pytest
from src.function_call_logger import FunctionCallLogger

class TestFunctionCallLogger:
    @FunctionCallLogger.log_calls
    def sample_function(self, x):
        return x * 2

    @FunctionCallLogger.log_calls
    def another_function(self):
        return "Hello"

    def test_function_call_logging(self):
        # Reset call counts before test
        FunctionCallLogger.reset_call_counts()

        # Call functions multiple times
        self.sample_function(5)
        self.sample_function(10)
        self.another_function()

        # Check call counts
        assert FunctionCallLogger.get_call_count('sample_function') == 2
        assert FunctionCallLogger.get_call_count('another_function') == 1

    def test_call_count_for_uncalled_function(self):
        # Reset call counts before test
        FunctionCallLogger.reset_call_counts()

        # Check count for a function that hasn't been called
        assert FunctionCallLogger.get_call_count('nonexistent_function') == 0

    def test_reset_call_counts(self):
        # Call some functions
        self.sample_function(3)
        self.another_function()

        # Reset call counts
        FunctionCallLogger.reset_call_counts()

        # Check that call counts are zeroed out
        assert FunctionCallLogger.get_call_count('sample_function') == 0
        assert FunctionCallLogger.get_call_count('another_function') == 0
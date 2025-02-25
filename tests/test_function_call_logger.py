import pytest
from src.function_call_logger import FunctionCallTracker

class TestFunctionCallTracker:
    def setup_method(self):
        # Reset call counts before each test
        FunctionCallTracker.reset_call_counts()

    @FunctionCallTracker.track
    def sample_function(self, x, y):
        return x + y

    @FunctionCallTracker.track
    def another_function(self):
        return "test"

    def test_function_call_count(self):
        # Test initial call count is zero
        assert FunctionCallTracker.get_call_count('sample_function') == 0
        assert FunctionCallTracker.get_call_count('another_function') == 0

        # Call functions multiple times
        self.sample_function(1, 2)
        self.sample_function(3, 4)
        self.another_function()

        # Verify call counts
        assert FunctionCallTracker.get_call_count('sample_function') == 2
        assert FunctionCallTracker.get_call_count('another_function') == 1

    def test_reset_call_counts(self):
        # Call functions
        self.sample_function(1, 2)
        self.another_function()

        # Reset call counts
        FunctionCallTracker.reset_call_counts()

        # Verify all call counts are zero
        assert FunctionCallTracker.get_call_count('sample_function') == 0
        assert FunctionCallTracker.get_call_count('another_function') == 0

    def test_return_value(self):
        # Ensure the original function's return value is preserved
        result1 = self.sample_function(5, 3)
        result2 = self.another_function()

        assert result1 == 8
        assert result2 == "test"
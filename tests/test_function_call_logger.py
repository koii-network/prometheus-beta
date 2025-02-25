import pytest
from src.function_call_logger import FunctionCallLogger

class TestFunctionCallLogger:
    def setup_method(self):
        """Reset call counts before each test"""
        FunctionCallLogger.reset_call_counts()

    @FunctionCallLogger.log_calls
    def sample_function(self, x: int) -> int:
        return x * 2

    @FunctionCallLogger.log_calls
    def another_function(self) -> str:
        return "Hello"

    def test_single_function_call(self):
        """Test call count for a single function call"""
        result = self.sample_function(5)
        assert result == 10
        assert FunctionCallLogger.get_call_count('sample_function') == 1

    def test_multiple_function_calls(self):
        """Test call count for multiple calls to the same function"""
        self.sample_function(1)
        self.sample_function(2)
        self.sample_function(3)
        assert FunctionCallLogger.get_call_count('sample_function') == 3

    def test_different_functions(self):
        """Test call counts for different functions"""
        self.sample_function(1)
        self.another_function()
        assert FunctionCallLogger.get_call_count('sample_function') == 1
        assert FunctionCallLogger.get_call_count('another_function') == 1

    def test_reset_call_counts(self):
        """Test resetting call counts"""
        self.sample_function(1)
        self.another_function()
        FunctionCallLogger.reset_call_counts()
        assert FunctionCallLogger.get_call_count('sample_function') == 0
        assert FunctionCallLogger.get_call_count('another_function') == 0

    def test_nonexistent_function_call_count(self):
        """Test getting call count for a function that hasn't been called"""
        assert FunctionCallLogger.get_call_count('nonexistent_function') == 0

    def test_function_return_value(self):
        """Ensure the decorated function returns the correct value"""
        result1 = self.sample_function(5)
        result2 = self.sample_function(10)
        assert result1 == 10
        assert result2 == 20
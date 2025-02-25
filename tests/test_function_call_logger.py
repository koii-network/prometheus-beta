import pytest
from src.function_call_logger import track_calls, FunctionCallTracker

class TestFunctionCallLogger:
    def setup_method(self):
        """Reset call counts before each test"""
        FunctionCallTracker.reset_call_counts()
    
    @track_calls
    def sample_function(self, x: int) -> int:
        """A sample function for testing call tracking"""
        return x * 2
    
    @track_calls
    def another_function(self) -> str:
        """Another sample function for testing call tracking"""
        return "test"
    
    def test_single_function_call(self):
        """Test tracking calls for a single function"""
        # Call the function once
        result = self.sample_function(5)
        
        # Check the result and call count
        assert result == 10
        assert FunctionCallTracker.get_call_count('sample_function') == 1
    
    def test_multiple_function_calls(self):
        """Test tracking multiple calls to the same function"""
        # Call the function multiple times
        self.sample_function(1)
        self.sample_function(2)
        self.sample_function(3)
        
        # Check the call count
        assert FunctionCallTracker.get_call_count('sample_function') == 3
    
    def test_multiple_functions(self):
        """Test tracking calls for multiple different functions"""
        # Call different functions
        self.sample_function(1)
        self.another_function()
        self.sample_function(2)
        self.another_function()
        
        # Check call counts for both functions
        assert FunctionCallTracker.get_call_count('sample_function') == 2
        assert FunctionCallTracker.get_call_count('another_function') == 2
    
    def test_reset_call_counts(self):
        """Test resetting call counts"""
        # Call functions
        self.sample_function(1)
        self.another_function()
        
        # Reset call counts
        FunctionCallTracker.reset_call_counts()
        
        # Check that counts are reset
        assert FunctionCallTracker.get_call_count('sample_function') == 0
        assert FunctionCallTracker.get_call_count('another_function') == 0
    
    def test_zero_calls(self):
        """Test getting call count for a function that hasn't been called"""
        # Check call count without calling the function
        assert FunctionCallTracker.get_call_count('nonexistent_function') == 0
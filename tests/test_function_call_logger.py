import pytest
from src.function_call_logger import FunctionCallTracker

class TestClass:
    @FunctionCallTracker.track_calls
    def example_method(self, x):
        return x * 2

    @FunctionCallTracker.track_calls
    def another_method(self, y):
        return y + 1

def test_function_call_tracking():
    # Reset call counts before testing
    FunctionCallTracker.reset_call_counts()
    
    # Create an instance of the test class
    test_obj = TestClass()
    
    # Call methods multiple times
    test_obj.example_method(5)
    test_obj.example_method(10)
    test_obj.another_method(3)
    
    # Check call counts
    assert FunctionCallTracker.get_call_count('example_method') == 2
    assert FunctionCallTracker.get_call_count('another_method') == 1

def test_reset_call_counts():
    # Ensure reset works correctly
    test_obj = TestClass()
    test_obj.example_method(5)
    
    # Reset call counts
    FunctionCallTracker.reset_call_counts()
    
    # Check that call counts are cleared
    assert FunctionCallTracker.get_call_count('example_method') == 0

def test_different_function_calls():
    # Reset call counts
    FunctionCallTracker.reset_call_counts()
    
    @FunctionCallTracker.track_calls
    def standalone_func():
        return 42
    
    # Call function multiple times
    standalone_func()
    standalone_func()
    standalone_func()
    
    # Check call count for standalone function
    assert FunctionCallTracker.get_call_count('standalone_func') == 3
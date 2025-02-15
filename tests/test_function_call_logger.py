import pytest
from src.function_call_logger import count_calls

def test_count_calls():
    # Create a sample function to test
    @count_calls
    def sample_function(x, y):
        return x + y
    
    # Verify initial call count is 0
    assert sample_function.get_call_count() == 0
    
    # Call the function multiple times
    sample_function(1, 2)
    assert sample_function.get_call_count() == 1
    
    sample_function(3, 4)
    assert sample_function.get_call_count() == 2
    
    # Verify the function still works correctly
    result = sample_function(5, 6)
    assert result == 11
    assert sample_function.get_call_count() == 3

def test_multiple_decorated_functions():
    # Test that different functions have independent call counts
    @count_calls
    def func1():
        pass
    
    @count_calls
    def func2():
        pass
    
    func1()
    func1()
    func2()
    
    assert func1.get_call_count() == 2
    assert func2.get_call_count() == 1

def test_function_with_args():
    @count_calls
    def func_with_args(a, b=None):
        return a + (b or 0)
    
    func_with_args(1)
    func_with_args(2, 3)
    func_with_args(a=4, b=5)
    
    assert func_with_args.get_call_count() == 3
import pytest
from src.function_call_logger import call_counter

def test_call_counter():
    # Test function to be decorated
    @call_counter
    def sample_function(x, y):
        return x + y
    
    # Initial call count should be 0
    assert sample_function.get_call_count() == 0
    
    # Call the function multiple times
    assert sample_function(2, 3) == 5
    assert sample_function.get_call_count() == 1
    
    # Call again
    sample_function(4, 5)
    assert sample_function.get_call_count() == 2
    
    # Reset call count
    sample_function.reset_call_count()
    assert sample_function.get_call_count() == 0

def test_multiple_decorated_functions():
    @call_counter
    def func1():
        return "func1"
    
    @call_counter
    def func2():
        return "func2"
    
    # Call functions in different orders
    func1()
    func1()
    func2()
    
    assert func1.get_call_count() == 2
    assert func2.get_call_count() == 1

def test_function_with_args_and_kwargs():
    @call_counter
    def complex_function(a, b=0, *args, **kwargs):
        return a + b
    
    complex_function(1)
    complex_function(2, 3)
    complex_function(4, b=5)
    
    assert complex_function.get_call_count() == 3
import time
import pytest
from src.execution_timer import measure_execution_time

def test_measure_execution_time_returns_correct_values():
    @measure_execution_time
    def sample_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y

    result, exec_time = sample_function(3, 4)
    
    assert result == 7  # Verify correct function execution
    assert 0.09 < exec_time < 0.11  # Check execution time is close to 0.1 seconds

def test_measure_execution_time_preserves_function_metadata():
    @measure_execution_time
    def test_func():
        """A test function docstring"""
        pass

    assert test_func.__name__ == 'test_func'
    assert test_func.__doc__ == 'A test function docstring'

def test_measure_execution_time_with_different_arguments():
    @measure_execution_time
    def multiply(a, b=1):
        return a * b

    result1, exec_time1 = multiply(5)
    result2, exec_time2 = multiply(5, 3)
    
    assert result1 == 5
    assert result2 == 15
    assert exec_time1 is not None
    assert exec_time2 is not None
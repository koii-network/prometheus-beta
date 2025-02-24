import pytest
import time
from src.execution_timer import measure_execution_time

def test_measure_execution_time_basic():
    """Test basic functionality of execution time measurement."""
    @measure_execution_time
    def simple_function(x, y):
        return x + y

    result, execution_time = simple_function(3, 4)
    
    assert result == 7
    assert isinstance(execution_time, float)
    assert execution_time >= 0

def test_measure_execution_time_with_delay():
    """Test execution time measurement with a small delay."""
    @measure_execution_time
    def delayed_function():
        time.sleep(0.1)
        return "delayed"

    result, execution_time = delayed_function()
    
    assert result == "delayed"
    assert execution_time >= 0.1
    assert execution_time < 0.2  # Allow some tolerance

def test_measure_execution_time_exception():
    """Test execution time measurement with a function that raises an exception."""
    @measure_execution_time
    def error_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        error_function()

def test_measure_execution_time_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        measure_execution_time("not a function")

def test_measure_execution_time_multiple_args():
    """Test execution time measurement with multiple arguments."""
    @measure_execution_time
    def multi_arg_function(a, b, c=10):
        return a * b + c

    result, execution_time = multi_arg_function(2, 3, c=5)
    
    assert result == 11
    assert isinstance(execution_time, float)
    assert execution_time >= 0

def test_measure_execution_time_no_args():
    """Test execution time measurement with a function that takes no arguments."""
    @measure_execution_time
    def no_arg_function():
        return "Hello"

    result, execution_time = no_arg_function()
    
    assert result == "Hello"
    assert isinstance(execution_time, float)
    assert execution_time >= 0
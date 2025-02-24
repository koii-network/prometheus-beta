import pytest
import time
from src.execution_timer import measure_execution_time

def test_measure_execution_time_basic():
    """Test basic functionality of the execution time decorator."""
    @measure_execution_time
    def simple_function():
        time.sleep(0.1)
        return 42

    result, execution_time = simple_function()
    
    assert result == 42
    assert 0.09 < execution_time < 0.11, f"Execution time was {execution_time}"

def test_measure_execution_time_with_args():
    """Test execution time decorator with function that takes arguments."""
    @measure_execution_time
    def multiply(a, b):
        time.sleep(0.05)
        return a * b

    result, execution_time = multiply(6, 7)
    
    assert result == 42
    assert 0.04 < execution_time < 0.06, f"Execution time was {execution_time}"

def test_measure_execution_time_error_handling():
    """Test error handling in the execution time decorator."""
    @measure_execution_time
    def raise_error():
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        raise_error()

def test_measure_execution_time_invalid_input():
    """Test that a TypeError is raised when input is not callable."""
    with pytest.raises(TypeError, match="Input must be a callable object"):
        measure_execution_time(42)

def test_measure_execution_time_zero_time():
    """Test execution time for an instant function."""
    @measure_execution_time
    def instant_function():
        return "quick"

    result, execution_time = instant_function()
    
    assert result == "quick"
    assert execution_time >= 0, f"Execution time was {execution_time}"
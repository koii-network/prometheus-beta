import time
import pytest
from src.execution_timer import measure_execution_time

def test_measure_execution_time_basic():
    """Test basic functionality of the execution time decorator."""
    @measure_execution_time
    def simple_function(x, y):
        return x + y
    
    # Call the decorated function
    result, exec_time = simple_function(3, 4)
    
    # Check result
    assert result == 7
    
    # Check execution time
    assert isinstance(exec_time, float)
    assert exec_time >= 0

def test_measure_execution_time_with_delay():
    """Test execution time measurement with a small delay."""
    @measure_execution_time
    def delayed_function():
        time.sleep(0.1)  # Delay for 0.1 seconds
        return "Done"
    
    # Call the decorated function
    result, exec_time = delayed_function()
    
    # Check result
    assert result == "Done"
    
    # Check execution time (should be close to 0.1)
    assert 0.09 < exec_time < 0.15

def test_measure_execution_time_preserves_function_metadata():
    """Ensure the decorator preserves function metadata."""
    @measure_execution_time
    def test_func():
        """Docstring test."""
        pass
    
    assert test_func.__name__ == 'test_func'
    assert test_func.__doc__ == 'Docstring test.'
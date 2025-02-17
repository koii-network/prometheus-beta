import pytest
import time
from src.execution_timer import measure_execution_time

def test_measure_execution_time(capsys):
    @measure_execution_time
    def slow_function():
        time.sleep(0.1)  # Simulate a slow function
    
    # Execute the function
    slow_function()
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that the output contains the function name and execution time
    assert 'slow_function' in captured.out
    assert 'took ' in captured.out
    assert 'seconds to execute' in captured.out

def test_measure_execution_time_with_args(capsys):
    @measure_execution_time
    def example_function(x, y):
        return x + y
    
    # Execute the function with arguments
    result = example_function(3, 4)
    
    # Verify the function works correctly
    assert result == 7
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that the output contains the function name and execution time
    assert 'example_function' in captured.out
    assert 'took ' in captured.out
    assert 'seconds to execute' in captured.out

def test_measure_execution_time_exception(capsys):
    @measure_execution_time
    def error_function():
        raise ValueError("Test exception")
    
    # Check that the original exception is raised
    with pytest.raises(ValueError, match="Test exception"):
        error_function()
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that the output contains the function name and execution time
    assert 'error_function' in captured.out
    assert 'raised an exception' in captured.out
    assert 'seconds' in captured.out
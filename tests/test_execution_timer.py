import time
import pytest
from src.execution_timer import measure_execution_time

def test_measure_execution_time_decorator(capsys):
    @measure_execution_time
    def simple_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y

    # Call the function
    result = simple_function(3, 4)
    
    # Check return value
    assert result == 7
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Check output contains function name and execution time
    assert "Function 'simple_function' took" in captured.out
    assert "seconds to execute" in captured.out

def test_measure_execution_time_with_exception(capsys):
    @measure_execution_time
    def error_function():
        time.sleep(0.05)  # Simulate some work
        raise ValueError("Test exception")

    # Expect the function to raise the original exception
    with pytest.raises(ValueError, match="Test exception"):
        error_function()
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Check output contains function name and exception timing
    assert "Function 'error_function' raised an exception" in captured.out
    assert "seconds" in captured.out

def test_measure_execution_time_no_args():
    @measure_execution_time
    def no_args_function():
        time.sleep(0.05)
        return "done"

    result = no_args_function()
    assert result == "done"

def test_measure_execution_time_with_kwargs():
    @measure_execution_time
    def kwargs_function(x=1, y=2):
        time.sleep(0.05)
        return x + y

    result = kwargs_function(x=3, y=4)
    assert result == 7
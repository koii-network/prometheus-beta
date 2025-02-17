import pytest
import time
from src.execution_timer import measure_execution_time

def test_measure_execution_time(capsys):
    @measure_execution_time
    def slow_function():
        time.sleep(0.1)  # Simulate a slow function
    
    @measure_execution_time
    def fast_function():
        return 42
    
    # Test slow function
    slow_function()
    captured = capsys.readouterr()
    assert "Function 'slow_function' took" in captured.out
    assert "seconds to execute" in captured.out
    
    # Test fast function
    result = fast_function()
    assert result == 42
    captured = capsys.readouterr()
    assert "Function 'fast_function' took" in captured.out
    
def test_execution_time_exception(capsys):
    @measure_execution_time
    def error_function():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError):
        error_function()
    
    captured = capsys.readouterr()
    assert "Function 'error_function' threw an exception" in captured.out
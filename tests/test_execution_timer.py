import pytest
import time
from src.execution_timer import measure_execution_time

def test_measure_execution_time_basic():
    """Test basic functionality of execution time measurement."""
    @measure_execution_time
    def simple_function(x: int, y: int) -> int:
        return x + y
    
    result, execution_time = simple_function(3, 4)
    
    assert result == 7
    assert isinstance(execution_time, float)
    assert execution_time >= 0

def test_measure_execution_time_with_delay():
    """Test execution time measurement with a deliberate delay."""
    @measure_execution_time
    def delayed_function():
        time.sleep(0.1)
        return "delayed"
    
    result, execution_time = delayed_function()
    
    assert result == "delayed"
    assert execution_time >= 0.1
    assert execution_time < 0.2  # Allow some buffer

def test_measure_execution_time_invalid_input():
    """Test error handling for invalid input."""
    with pytest.raises(TypeError):
        measure_execution_time(None)  # type: ignore

def test_measure_execution_time_preserves_metadata():
    """Ensure the decorator preserves function metadata."""
    @measure_execution_time
    def sample_function(x: int) -> int:
        """A sample docstring."""
        return x * 2
    
    assert sample_function.__name__ == 'sample_function'
    assert 'A sample docstring.' in sample_function.__doc__
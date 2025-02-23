import pytest
from src.fibonacci_sum import fibonacci_sequence_sum

def test_fibonacci_sequence_sum_basic():
    """Test basic functionality of the function."""
    assert fibonacci_sequence_sum(1) == 0
    assert fibonacci_sequence_sum(2) == 1
    assert fibonacci_sequence_sum(3) == 1
    assert fibonacci_sequence_sum(4) == 2
    assert fibonacci_sequence_sum(5) == 4
    assert fibonacci_sequence_sum(6) == 7

def test_fibonacci_sequence_sum_larger_n():
    """Test larger input values."""
    assert fibonacci_sequence_sum(10) == 88

def test_fibonacci_sequence_sum_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum("not a number")
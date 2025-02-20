import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic():
    """Test basic functionality for known Fibonacci sum values."""
    assert fibonacci_sum(1) == 0  # First Fibonacci number
    assert fibonacci_sum(2) == 1  # 0 + 1
    assert fibonacci_sum(3) == 1  # 0 + 1 + 0
    assert fibonacci_sum(4) == 2  # 0 + 1 + 0 + 1
    assert fibonacci_sum(5) == 4  # 0 + 1 + 0 + 1 + 2
    assert fibonacci_sum(6) == 7  # 0 + 1 + 0 + 1 + 2 + 3

def test_fibonacci_sum_larger_n():
    """Test Fibonacci sum for larger number of terms."""
    assert fibonacci_sum(10) == 88

def test_fibonacci_sum_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("5")
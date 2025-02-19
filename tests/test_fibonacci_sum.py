import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic():
    """Test basic functionality of fibonacci_sum"""
    assert fibonacci_sum(1) == 0
    assert fibonacci_sum(2) == 1
    assert fibonacci_sum(3) == 1
    assert fibonacci_sum(4) == 2
    assert fibonacci_sum(5) == 4
    assert fibonacci_sum(6) == 7

def test_fibonacci_sum_larger_numbers():
    """Test fibonacci_sum with larger input values"""
    assert fibonacci_sum(10) == 88
    assert fibonacci_sum(15) == 1597

def test_fibonacci_sum_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("not a number")
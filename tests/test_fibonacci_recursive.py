import pytest
from src.fibonacci_recursive import fibonacci_recursive

def test_fibonacci_base_cases():
    """Test the base cases for Fibonacci sequence"""
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1

def test_fibonacci_early_sequence():
    """Test early Fibonacci numbers"""
    assert fibonacci_recursive(3) == 2  # 1 + 1
    assert fibonacci_recursive(4) == 3  # 1 + 2
    assert fibonacci_recursive(5) == 5  # 2 + 3
    assert fibonacci_recursive(6) == 8  # 3 + 5

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers"""
    assert fibonacci_recursive(7) == 13
    assert fibonacci_recursive(10) == 55

def test_fibonacci_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_recursive(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_recursive(-1)
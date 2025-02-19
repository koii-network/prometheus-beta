import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic_cases():
    # Test first few known Fibonacci sums
    assert fibonacci_sum(1) == 0   # First Fibonacci number is 0
    assert fibonacci_sum(2) == 1   # Sum of first two Fibonacci numbers: 0 + 1
    assert fibonacci_sum(3) == 1   # 0 + 1 + 0
    assert fibonacci_sum(4) == 2   # 0 + 1 + 0 + 1
    assert fibonacci_sum(5) == 4   # 0 + 1 + 0 + 1 + 2
    assert fibonacci_sum(6) == 7   # 0 + 1 + 0 + 1 + 2 + 3

def test_fibonacci_sum_larger_input():
    # Test larger input values
    assert fibonacci_sum(10) == 88
    assert fibonacci_sum(15) == 610

def test_fibonacci_sum_invalid_input():
    # Test invalid input handling
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("not a number")
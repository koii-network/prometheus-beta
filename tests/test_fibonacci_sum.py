import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_standard_cases():
    # Test first few known cases
    assert fibonacci_sum(1) == 0
    assert fibonacci_sum(2) == 1
    assert fibonacci_sum(3) == 1  # 0 + 1 + 0
    assert fibonacci_sum(4) == 2  # 0 + 1 + 0 + 1
    assert fibonacci_sum(5) == 4  # 0 + 1 + 0 + 1 + 2

def test_fibonacci_sum_larger_cases():
    # Test some larger Fibonacci sum sequences
    assert fibonacci_sum(6) == 7   # 0 + 1 + 0 + 1 + 2 + 3
    assert fibonacci_sum(10) == 88  # Longer Fibonacci sum

def test_fibonacci_sum_invalid_input():
    # Test error handling
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("not a number")
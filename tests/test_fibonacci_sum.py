import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_positive_cases():
    # Test known sum values
    assert fibonacci_sum(1) == 0     # First Fibonacci number
    assert fibonacci_sum(2) == 1     # Sum of first two (0 + 1)
    assert fibonacci_sum(3) == 2     # 0 + 1 + 1
    assert fibonacci_sum(4) == 4     # 0 + 1 + 1 + 2
    assert fibonacci_sum(5) == 7     # 0 + 1 + 1 + 2 + 3
    assert fibonacci_sum(6) == 12    # 0 + 1 + 1 + 2 + 3 + 5

def test_fibonacci_sum_error_cases():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("3")

def test_fibonacci_sum_large_n():
    # Test a larger input to ensure calculation works for bigger numbers
    assert fibonacci_sum(10) == 88  # Sum of first 10 Fibonacci numbers
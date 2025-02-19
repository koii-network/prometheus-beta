import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_valid_inputs():
    # Test initial values
    assert fibonacci_sum(1) == 0  # First Fibonacci number is 0
    assert fibonacci_sum(2) == 1  # Sum of first two (0 + 1)
    assert fibonacci_sum(3) == 1  # Sum of first three (0 + 1 + 0)
    assert fibonacci_sum(4) == 2  # Sum of first four (0 + 1 + 0 + 1)
    assert fibonacci_sum(5) == 3  # Sum of first five (0 + 1 + 0 + 1 + 1)

def test_fibonacci_sum_larger_inputs():
    assert fibonacci_sum(10) == 88  # Sum of first 10 Fibonacci numbers
    assert fibonacci_sum(15) == 610  # Sum of first 15 Fibonacci numbers

def test_fibonacci_sum_invalid_inputs():
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_sum("5")
    
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_sum([])
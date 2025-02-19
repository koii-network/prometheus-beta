import pytest
from src.fibonacci_recursive import fibonacci

def test_fibonacci_base_cases():
    # Test first two Fibonacci numbers
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1

def test_fibonacci_known_values():
    # Test known Fibonacci sequence values
    assert fibonacci(3) == 2  # 1 + 1
    assert fibonacci(4) == 3  # 1 + 2
    assert fibonacci(5) == 5  # 2 + 3
    assert fibonacci(6) == 8  # 3 + 5
    assert fibonacci(7) == 13  # 5 + 8

def test_fibonacci_invalid_input():
    # Test invalid input raises ValueError
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(-1)
        
def test_fibonacci_large_input():
    # Test a larger Fibonacci number
    assert fibonacci(10) == 55
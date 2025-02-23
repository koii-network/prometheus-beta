import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    # Test base cases
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    # Test known Fibonacci sequence values
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55

def test_fibonacci_invalid_input():
    # Test negative input
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative indices"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
        fibonacci("5")
        fibonacci(None)
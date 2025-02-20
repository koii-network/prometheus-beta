import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_small_numbers():
    """Test Fibonacci numbers for small inputs."""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger inputs."""
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)

def test_fibonacci_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(None)
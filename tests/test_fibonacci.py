import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test Fibonacci numbers for known values."""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(10) == 55

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger indices."""
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040
    assert fibonacci(40) == 102334155

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-100)

def test_fibonacci_invalid_input_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(None)
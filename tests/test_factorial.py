import pytest
from src.factorial import calculate_factorial

def test_factorial_zero():
    """Test factorial of 0 is 1."""
    assert calculate_factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1 is 1."""
    assert calculate_factorial(1) == 1

def test_factorial_positive_number():
    """Test factorial of a typical positive number."""
    assert calculate_factorial(5) == 120
    assert calculate_factorial(6) == 720

def test_factorial_negative_number():
    """Test that calculating factorial of a negative number raises ValueError."""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_factorial_non_integer():
    """Test that non-integer inputs raise TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")
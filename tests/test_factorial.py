import pytest
from src.factorial import calculate_factorial

def test_factorial_zero():
    """Test factorial of 0."""
    assert calculate_factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1."""
    assert calculate_factorial(1) == 1

def test_factorial_positive_number():
    """Test factorial of a positive number."""
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800

def test_factorial_large_number():
    """Test factorial of a large number."""
    assert calculate_factorial(20) == 2432902008176640000

def test_factorial_negative_number():
    """Test that a negative number raises a ValueError."""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_factorial_non_integer():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial([5])
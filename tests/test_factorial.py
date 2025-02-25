import pytest
from src.factorial import calculate_factorial

def test_factorial_zero():
    """Test factorial of 0 is 1"""
    assert calculate_factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1 is 1"""
    assert calculate_factorial(1) == 1

def test_factorial_positive_number():
    """Test factorial of a positive number"""
    assert calculate_factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120

def test_factorial_large_number():
    """Test factorial of a larger number"""
    assert calculate_factorial(10) == 3628800  # 10! = 3,628,800

def test_factorial_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_factorial_invalid_input_type():
    """Test that non-integer input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")
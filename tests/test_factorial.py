import pytest
from src.factorial import calculate_factorial

def test_factorial_zero():
    """Test factorial of 0 returns 1"""
    assert calculate_factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1 returns 1"""
    assert calculate_factorial(1) == 1

def test_factorial_positive_number():
    """Test factorial of a positive number"""
    assert calculate_factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120

def test_factorial_large_number():
    """Test factorial of a larger number"""
    assert calculate_factorial(10) == 3628800  # 10! = 3,628,800

def test_negative_number_raises_error():
    """Test that a negative number raises a ValueError"""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calculate_factorial(-1)

def test_non_integer_input_raises_error():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_factorial(None)
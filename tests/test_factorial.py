import pytest
from src.factorial import factorial

def test_factorial_zero():
    """Test factorial of 0 is 1"""
    assert factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1 is 1"""
    assert factorial(1) == 1

def test_factorial_positive_numbers():
    """Test factorial of various positive numbers"""
    assert factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1
    assert factorial(3) == 6    # 3! = 3 * 2 * 1

def test_factorial_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial(-1)

def test_factorial_non_integer_input():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        factorial(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        factorial("5")
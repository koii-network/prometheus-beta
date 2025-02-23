import pytest
from src.factorial import factorial

def test_factorial_zero():
    """Test factorial of 0 returns 1."""
    assert factorial(0) == 1

def test_factorial_one():
    """Test factorial of 1 returns 1."""
    assert factorial(1) == 1

def test_factorial_positive():
    """Test factorial of several positive numbers."""
    assert factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1
    assert factorial(3) == 6    # 3! = 3 * 2 * 1
    assert factorial(7) == 7 * 6 * 5 * 4 * 3 * 2 * 1

def test_factorial_negative():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial(-1)

def test_factorial_non_integer():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        factorial(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        factorial("5")

def test_factorial_large_number():
    """Test a larger number to check for potential recursion issues."""
    assert factorial(10) == 3628800  # 10!
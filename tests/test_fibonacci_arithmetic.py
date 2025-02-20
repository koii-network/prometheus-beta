import pytest
from src.fibonacci_arithmetic import find_fibonacci_arithmetic_progression

def test_fibonacci_arithmetic_progression_basic():
    """Test a basic arithmetic progression of Fibonacci numbers"""
    result = find_fibonacci_arithmetic_progression(3)
    assert result == [1, 1, 2], "First 3 Fibonacci numbers should form an arithmetic progression"

def test_fibonacci_arithmetic_progression_not_found():
    """Test when no arithmetic progression is found"""
    result = find_fibonacci_arithmetic_progression(4)
    assert result == [], "No arithmetic progression should return an empty list"

def test_fibonacci_arithmetic_progression_invalid_input():
    """Test invalid input less than 3"""
    with pytest.raises(ValueError, match="At least 3 numbers are required"):
        find_fibonacci_arithmetic_progression(2)

def test_fibonacci_arithmetic_progression_larger():
    """Test with larger sequence"""
    result = find_fibonacci_arithmetic_progression(5)
    assert result == [], "Should return an empty list for 5 Fibonacci numbers"
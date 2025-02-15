import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers"""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test non-perfect numbers"""
    non_perfect_numbers = [10, 15, 21, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-5)
    
    # Test zero
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("not a number")
import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares"""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) == True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares"""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 15, 26, 50, 99]
    for num in non_perfect_squares:
        assert is_perfect_square(num) == False, f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square"""
    large_square = 1000000  # 1000^2
    assert is_perfect_square(large_square) == True

def test_input_validation():
    """Test input validation"""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_perfect_square(-4)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square("16")
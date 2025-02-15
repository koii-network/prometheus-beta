import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various perfect squares"""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 10000]
    for num in perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares"""
    non_perfect_squares = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17]
    for num in non_perfect_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"

def test_edge_cases():
    """Test edge case scenarios"""
    # Test zero and one
    assert is_perfect_square(0)
    assert is_perfect_square(1)

def test_large_square():
    """Test a large perfect square"""
    large_square = 1_000_000  # 1000 squared
    assert is_perfect_square(large_square)

def test_input_validation():
    """Test input validation"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_perfect_square(-4)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square("16")
import pytest
import math
from src.perfect_square_check import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares"""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) == True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares"""
    non_perfect_squares = [2, 3, 5, 6, 7, 8, 10, 12, 15]
    for num in non_perfect_squares:
        assert is_perfect_square(num) == False, f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square"""
    large_square = 10000  # 100^2
    assert is_perfect_square(large_square) == True

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        is_perfect_square(3.14)
    with pytest.raises(TypeError):
        is_perfect_square("16")
    with pytest.raises(TypeError):
        is_perfect_square(None)

def test_negative_numbers():
    """Test negative numbers"""
    with pytest.raises(ValueError):
        is_perfect_square(-4)
    with pytest.raises(ValueError):
        is_perfect_square(-1)
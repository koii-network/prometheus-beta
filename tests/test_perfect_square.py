import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares"""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) == True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test known non-perfect squares"""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 12, 26, 45, 99]
    for num in non_perfect_squares:
        assert is_perfect_square(num) == False, f"{num} should not be a perfect square"

def test_large_perfect_squares():
    """Test some larger perfect squares"""
    large_squares = [10000, 1000000, 123321 * 123321]
    for num in large_squares:
        assert is_perfect_square(num) == True, f"{num} should be a perfect square"

def test_zero_and_one():
    """Test edge cases 0 and 1"""
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True

def test_type_error():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError):
        is_perfect_square(3.14)
    with pytest.raises(TypeError):
        is_perfect_square("16")
    with pytest.raises(TypeError):
        is_perfect_square([16])

def test_negative_numbers():
    """Test that negative numbers raise ValueError"""
    with pytest.raises(ValueError):
        is_perfect_square(-4)
    with pytest.raises(ValueError):
        is_perfect_square(-1)
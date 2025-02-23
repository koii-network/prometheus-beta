import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various perfect squares"""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares"""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 15, 17, 26, 99]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_floating_point_perfect_squares():
    """Test floating point perfect squares"""
    assert is_perfect_square(4.0) is True
    assert is_perfect_square(9.0) is True
    assert is_perfect_square(16.0) is True

def test_floating_point_near_perfect_squares():
    """Test floating point numbers close to but not exactly perfect squares"""
    assert is_perfect_square(4.000001) is False
    assert is_perfect_square(8.999999) is False

def test_zero_and_one():
    """Test special cases of 0 and 1"""
    assert is_perfect_square(0) is True
    assert is_perfect_square(1) is True

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
    
    # Test non-numeric inputs
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square([16])
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square(None)
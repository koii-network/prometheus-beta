import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 10, 15, 20, 26, 33, 99]
    for num in non_perfect_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"

def test_floating_point_perfect_squares():
    """Test floating point perfect squares."""
    assert is_perfect_square(4.0), "4.0 should be a perfect square"
    assert not is_perfect_square(5.5), "5.5 should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    large_perfect_square = 1000000  # 1000^2
    assert is_perfect_square(large_perfect_square), f"{large_perfect_square} should be a perfect square"

def test_zero_and_one():
    """Test special cases 0 and 1."""
    assert is_perfect_square(0), "0 should be a perfect square"
    assert is_perfect_square(1), "1 should be a perfect square"

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a numeric type"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a numeric type"):
        is_perfect_square([16])
    with pytest.raises(TypeError, match="Input must be a numeric type"):
        is_perfect_square(None)
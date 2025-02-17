import pytest
import math
from src.perfect_square_checker import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 12, 15, 17, 20]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_floating_point_perfect_squares():
    """Test perfect squares with floating point precision."""
    assert is_perfect_square(25.0) is True
    assert is_perfect_square(16.0) is True

def test_floating_point_non_perfect_squares():
    """Test non-perfect squares with floating point precision."""
    assert is_perfect_square(7.5) is False
    assert is_perfect_square(10.1) is False

def test_large_perfect_square():
    """Test a large perfect square."""
    large_square = 10000  # 100^2
    assert is_perfect_square(large_square) is True

def test_negative_number_raises_value_error():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)

def test_non_numeric_input_raises_type_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square([4])
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square(None)
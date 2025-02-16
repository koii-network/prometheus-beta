import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 10, 15, 17, 26, 42]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False

def test_floating_point_perfect_squares():
    """Test floating point perfect squares."""
    assert is_perfect_square(4.0) is True
    assert is_perfect_square(9.0) is True
    assert is_perfect_square(16.0) is True

def test_floating_point_non_perfect_squares():
    """Test floating point non-perfect squares."""
    assert is_perfect_square(2.5) is False
    assert is_perfect_square(3.14) is False

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError):
        is_perfect_square(-4)
    with pytest.raises(ValueError):
        is_perfect_square(-1)

def test_invalid_input():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        is_perfect_square("16")
    with pytest.raises(TypeError):
        is_perfect_square([16])
    with pytest.raises(TypeError):
        is_perfect_square(None)

def test_large_perfect_square():
    """Test a large perfect square."""
    large_perfect_square = 10000 * 10000
    assert is_perfect_square(large_perfect_square) is True
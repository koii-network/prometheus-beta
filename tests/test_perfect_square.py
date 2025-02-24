import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 10, 11, 12, 13, 15, 17, 99]
    for num in non_perfect_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"

def test_float_perfect_squares():
    """Test float perfect squares."""
    float_perfect_squares = [4.0, 9.0, 16.0, 25.0]
    for num in float_perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_float_non_perfect_squares():
    """Test float non-perfect squares."""
    float_non_perfect_squares = [2.5, 3.7, 5.1, 7.2]
    for num in float_non_perfect_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"

def test_invalid_input_types():
    """Test invalid input types."""
    invalid_inputs = ['string', [1, 2, 3], {'key': 'value'}, None]
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError, match="Input must be a number"):
            is_perfect_square(invalid_input)

def test_negative_numbers():
    """Test negative number input."""
    negative_numbers = [-1, -4, -9, -16]
    for num in negative_numbers:
        with pytest.raises(ValueError, match="Input must be a non-negative number"):
            is_perfect_square(num)

def test_large_perfect_squares():
    """Test larger perfect squares."""
    large_perfect_squares = [10000, 1000000, 10**8, 10**12]
    for num in large_perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"
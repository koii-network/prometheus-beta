import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test various non-perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 10, 14, 15, 23, 26]
    for num in non_perfect_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    large_square = 123454321
    assert is_perfect_square(large_square), f"{large_square} should be a perfect square"

def test_input_type_errors():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_perfect_square(3.14)
    with pytest.raises(TypeError):
        is_perfect_square("16")
    with pytest.raises(TypeError):
        is_perfect_square([16])

def test_negative_number_error():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError):
        is_perfect_square(-4)
    with pytest.raises(ValueError):
        is_perfect_square(-1)
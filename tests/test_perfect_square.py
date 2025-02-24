import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for square in perfect_squares:
        assert is_perfect_square(square) == True, f"{square} should be a perfect square"

def test_non_perfect_squares():
    """Test various numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 12, 15, 17, 20]
    for number in non_perfect_squares:
        assert is_perfect_square(number) == False, f"{number} should not be a perfect square"

def test_zero_and_one():
    """Test edge cases of 0 and 1."""
    assert is_perfect_square(0) == True, "0 should be considered a perfect square"
    assert is_perfect_square(1) == True, "1 should be considered a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    large_square = 1000000  # 1000^2
    assert is_perfect_square(large_square) == True, f"{large_square} should be a perfect square"

def test_negative_number():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_perfect_square(-4)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_perfect_square(-1)

def test_float_input():
    """Ensure the function only accepts integers."""
    with pytest.raises(TypeError):
        is_perfect_square(4.5)
    with pytest.raises(TypeError):
        is_perfect_square(math.pi)
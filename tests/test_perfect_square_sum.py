import pytest
import math
from src.perfect_square_sum import sum_perfect_squares_from_set

def test_basic_perfect_squares():
    """Test basic set of integers with perfect squares."""
    assert sum_perfect_squares_from_set({1, 2, 3}) == 5  # 1^2 + 2^2
    assert sum_perfect_squares_from_set({4, 9}) == 13  # 2^2 + 3^2

def test_empty_set():
    """Test with an empty set."""
    assert sum_perfect_squares_from_set(set()) == 0

def test_no_perfect_squares():
    """Test a set with no perfect squares."""
    assert sum_perfect_squares_from_set({5, 7, 11}) == 0

def test_multiple_perfect_squares():
    """Test a set with multiple perfect squares."""
    result = sum_perfect_squares_from_set({1, 2, 3, 4, 9})
    assert result == 20  # 1^2 + 2^2 + 3^2 + 4^2

def test_large_perfect_squares():
    """Test with larger perfect squares."""
    result = sum_perfect_squares_from_set({16, 25, 36})
    assert result == 77  # 4^2 + 5^2 + 6^2

def test_duplicate_squares():
    """Test that duplicate squares are not counted multiple times."""
    assert sum_perfect_squares_from_set({4, 4, 9}) == 13

def test_invalid_input_type():
    """Test that TypeError is raised for non-set input."""
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set([1, 2, 3])  # list instead of set

def test_negative_numbers():
    """Test that ValueError is raised for negative numbers."""
    with pytest.raises(ValueError):
        sum_perfect_squares_from_set({-1, 2, 3})

def test_mixed_numbers():
    """Test a mix of perfect squares and non-perfect squares."""
    result = sum_perfect_squares_from_set({1, 2, 5, 9, 16})
    assert result == 42  # 1^2 + 2^2 + 3^2 + 4^2
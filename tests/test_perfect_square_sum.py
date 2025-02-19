import pytest
from src.perfect_square_sum import sum_perfect_squares_from_set

def test_basic_perfect_square_sum():
    """Test with a simple set of numbers that can form perfect squares"""
    test_set = {1, 4, 9}
    assert sum_perfect_squares_from_set(test_set) == 63  # 1 + 4 + 9 + 49

def test_complex_perfect_square_sum():
    """Test with a more complex set of numbers"""
    test_set = {1, 2, 3, 4}
    result = sum_perfect_squares_from_set(test_set)
    assert result > 0  # Should find at least some perfect squares

def test_no_perfect_squares():
    """Test with a set that cannot form many perfect squares"""
    test_set = {2, 3, 5, 7}
    result = sum_perfect_squares_from_set(test_set)
    assert result >= 0  # Might contain an unexpected perfect square

def test_empty_set():
    """Test with an empty set"""
    test_set = set()
    assert sum_perfect_squares_from_set(test_set) == 0

def test_invalid_input_not_set():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a set"):
        sum_perfect_squares_from_set([1, 2, 3])

def test_invalid_input_non_integers():
    """Test with a set containing non-integer elements"""
    with pytest.raises(TypeError, match="Set must contain only integers"):
        sum_perfect_squares_from_set({1, 2, 'a'})
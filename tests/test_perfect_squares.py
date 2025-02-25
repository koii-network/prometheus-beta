import pytest
from src.perfect_squares import sum_perfect_squares_from_set

def test_basic_perfect_squares():
    # Basic test with some perfect squares
    assert sum_perfect_squares_from_set({1, 2, 3, 4}) == 30  # 1, 4, 9, 16
    
def test_empty_set():
    # Empty set should return 0
    assert sum_perfect_squares_from_set(set()) == 0

def test_no_perfect_squares():
    # Set with no perfect squares
    assert sum_perfect_squares_from_set({5, 7, 11}) == 0

def test_mixed_values():
    # Mixed set with some perfect squares
    assert sum_perfect_squares_from_set({1, 2, 3, 5, 6}) == 30  # 1, 4, 9, 16

def test_negative_and_non_integer():
    # Test handling of negative and non-integer values
    assert sum_perfect_squares_from_set({-1, 2, 3, 'a', 4}) == 30  # should ignore -1 and 'a'

def test_invalid_input():
    # Test that non-set input raises TypeError
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set([1, 2, 3])  # list instead of set
import pytest
from src.perfect_square_sum import sum_perfect_squares

def test_basic_perfect_square_sum():
    # Test basic scenario with some perfect squares
    result = sum_perfect_squares({1, 2, 3, 4})
    assert result == 14  # 1*1 = 1, 2*2 = 4, 3*3 = 9 => 1 + 4 + 9 = 14

def test_no_perfect_squares():
    # Test scenario with no perfect squares
    result = sum_perfect_squares({5, 7, 11})
    assert result == 0

def test_empty_set():
    # Test empty set
    result = sum_perfect_squares(set())
    assert result == 0

def test_large_set():
    # Test a larger set with multiple perfect squares
    result = sum_perfect_squares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    assert result == 110  # Sum of 1, 4, 9, 16, 25, 36, 49, 64

def test_invalid_input_type():
    # Test invalid input type
    with pytest.raises(TypeError):
        sum_perfect_squares([1, 2, 3])  # List instead of set

def test_negative_and_non_integer_input():
    # Test set with negative and non-integer elements
    result = sum_perfect_squares({-1, 2, 'a', 3, 4})
    assert result == 14  # Only consider 2, 3, 4
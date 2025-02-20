import pytest
from src.max_non_adjacent_sum import max_non_adjacent_digits_sum

def test_max_non_adjacent_digits_sum_basic():
    assert max_non_adjacent_digits_sum(1234) == 7  # 1 + 3 = 4
    assert max_non_adjacent_digits_sum(2468) == 12  # 2 + 4 + 6 = 12
    assert max_non_adjacent_digits_sum(1111) == 2  # 1 + 1 = 2

def test_max_non_adjacent_digits_sum_single_digit():
    assert max_non_adjacent_digits_sum(5) == 5
    assert max_non_adjacent_digits_sum(0) == 0

def test_max_non_adjacent_digits_sum_two_digits():
    assert max_non_adjacent_digits_sum(42) == 6  # 4 or 2
    assert max_non_adjacent_digits_sum(97) == 9  # 9

def test_max_non_adjacent_digits_sum_error_handling():
    with pytest.raises(ValueError):
        max_non_adjacent_digits_sum(-1)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digits_sum("123")

def test_max_non_adjacent_digits_sum_complex_cases():
    assert max_non_adjacent_digits_sum(9876) == 16  # 9 + 7 = 16
    assert max_non_adjacent_digits_sum(10101) == 11  # 1 + 1 + 9 = 11
    assert max_non_adjacent_digits_sum(54321) == 9  # 5 + 4 = 9
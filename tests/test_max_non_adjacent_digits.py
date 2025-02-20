import pytest
from src.max_non_adjacent_digits import max_non_adjacent_digit_sum

def test_single_digit_number():
    assert max_non_adjacent_digit_sum(5) == 5

def test_two_digit_number():
    assert max_non_adjacent_digit_sum(42) == 6  # Chooses max between 4 and 2
    assert max_non_adjacent_digit_sum(99) == 9  # Chooses the maximum digit

def test_multi_digit_numbers():
    assert max_non_adjacent_digit_sum(123) == 13  # 1 + 2 with space between
    assert max_non_adjacent_digit_sum(1234) == 17  # 1 + 2 + 4
    assert max_non_adjacent_digit_sum(7654) == 19  # 7 + 6 + 6
    assert max_non_adjacent_digit_sum(9876) == 25  # 9 + 8 + 8

def test_larger_numbers():
    assert max_non_adjacent_digit_sum(10203040) == 14  # 1 + 3 + 0 + 0
    assert max_non_adjacent_digit_sum(2022) == 22  # 2 + 2 + 2

def test_invalid_inputs():
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(0)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(-123)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum('123')  # Not an integer
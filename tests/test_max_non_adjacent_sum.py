import pytest
from src.max_non_adjacent_sum import max_non_adjacent_digit_sum

def test_single_digit():
    assert max_non_adjacent_digit_sum(5) == 5

def test_two_digits():
    assert max_non_adjacent_digit_sum(54) == 5
    assert max_non_adjacent_digit_sum(45) == 5

def test_multiple_digits():
    assert max_non_adjacent_digit_sum(1234) == 6  # 1 + 5
    assert max_non_adjacent_digit_sum(5786) == 11  # 5 + 6
    assert max_non_adjacent_digit_sum(9876) == 15  # 9 + 6

def test_all_same_digits():
    assert max_non_adjacent_digit_sum(9999) == 18  # 9 + 9
    assert max_non_adjacent_digit_sum(1111) == 2  # 1 + 1

def test_large_number():
    assert max_non_adjacent_digit_sum(123456789) == 20  # 1 + 3 + 5 + 7 + 9

def test_invalid_input():
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(0)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(-5)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(3.14)
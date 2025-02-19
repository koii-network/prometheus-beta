import pytest
from src.missing_numbers import find_missing_numbers

def test_ascending_missing_numbers():
    assert find_missing_numbers([1, 2, 4, 6, 7, 9, 10]) == [3, 5, 8]

def test_descending_missing_numbers():
    assert find_missing_numbers([10, 9, 7, 6, 4, 2, 1]) == [8, 5, 3]

def test_no_missing_numbers():
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_single_number():
    assert find_missing_numbers([1]) == []

def test_empty_list():
    assert find_missing_numbers([]) == []

def test_non_list_input():
    with pytest.raises(ValueError, match="Input must be a list"):
        find_missing_numbers(123)

def test_non_positive_integers():
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_missing_numbers([1, 2, -3, 4])

def test_large_range_of_numbers():
    assert find_missing_numbers([1, 3, 5, 10, 11, 13, 15]) == [2, 4, 6, 7, 8, 9, 12, 14]
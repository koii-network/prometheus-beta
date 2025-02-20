import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test basic scenario with missing numbers"""
    assert find_missing_numbers([1, 3, 5, 10]) == [2, 4, 6, 7, 8, 9]

def test_find_missing_numbers_no_missing():
    """Test scenario with no missing numbers"""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_find_missing_numbers_single_element():
    """Test scenario with a single element"""
    assert find_missing_numbers([5]) == []

def test_find_missing_numbers_large_gap():
    """Test scenario with a large gap between numbers"""
    assert find_missing_numbers([10, 20]) == list(range(11, 20))

def test_find_missing_numbers_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])
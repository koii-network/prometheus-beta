import pytest
from src.missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test basic scenario with some missing numbers"""
    arr = [1, 2, 4, 6, 7, 10]
    assert find_missing_numbers(arr) == [3, 5, 8, 9]

def test_find_missing_numbers_no_gaps():
    """Test scenario where no numbers are missing"""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_large_range():
    """Test scenario with a larger range of numbers"""
    arr = [10, 11, 13, 15, 16, 19, 20]
    assert find_missing_numbers(arr) == [12, 14, 17, 18]

def test_find_missing_numbers_single_element():
    """Test scenario with a single element array"""
    arr = [5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_error_empty_list():
    """Test error handling for empty list"""
    with pytest.raises(ValueError, match="Input must be a non-empty list of unique integers"):
        find_missing_numbers([])

def test_find_missing_numbers_error_non_list():
    """Test error handling for non-list input"""
    with pytest.raises(ValueError, match="Input must be a non-empty list of unique integers"):
        find_missing_numbers("not a list")

def test_find_missing_numbers_error_non_unique():
    """Test error handling for non-unique input"""
    with pytest.raises(ValueError, match="Input must contain unique integers"):
        find_missing_numbers([1, 2, 2, 3])
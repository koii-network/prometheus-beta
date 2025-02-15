import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_find_single_non_duplicate_basic():
    # Basic test case
    arr = [1, 1, 2, 3, 3, 4, 4, 5, 5]
    assert find_single_non_duplicate(arr) == 2

def test_find_single_non_duplicate_at_start():
    # Unique element at the start
    arr = [1, 2, 2, 3, 3, 4, 4]
    assert find_single_non_duplicate(arr) == 1

def test_find_single_non_duplicate_at_end():
    # Unique element at the end
    arr = [1, 1, 2, 2, 3, 3, 4]
    assert find_single_non_duplicate(arr) == 4

def test_find_single_non_duplicate_single_element():
    # Array with a single element
    arr = [7]
    assert find_single_non_duplicate(arr) == 7

def test_find_single_non_duplicate_large_array():
    # Larger array with a unique element
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
    assert find_single_non_duplicate(arr) == 7

def test_find_single_non_duplicate_empty_array():
    # Empty array should raise ValueError
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_single_non_duplicate([])

def test_find_single_non_duplicate_no_unique_element():
    # Array with no unique element should raise ValueError
    with pytest.raises(ValueError, match="No single non-duplicate element found"):
        find_single_non_duplicate([1, 1, 2, 2])
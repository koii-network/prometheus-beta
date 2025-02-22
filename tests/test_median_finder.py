import pytest
from src.median_finder import find_median_index

def test_odd_length_array():
    # Test with an odd-length array
    test_arr = [1, 2, 3, 4, 5]
    assert find_median_index(test_arr) == 2

def test_even_length_array():
    # Test with an even-length array
    test_arr = [1, 2, 3, 4]
    assert find_median_index(test_arr) == 1.5

def test_single_element_array():
    # Test with a single-element array
    test_arr = [42]
    assert find_median_index(test_arr) == 0

def test_empty_array():
    # Test that an empty array raises a ValueError
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_median_index([])

def test_larger_array():
    # Test with a larger odd-length array
    test_arr = [10, 20, 30, 40, 50, 60, 70]
    assert find_median_index(test_arr) == 3

def test_larger_even_array():
    # Test with a larger even-length array
    test_arr = [10, 20, 30, 40, 50, 60]
    assert find_median_index(test_arr) == 2.5
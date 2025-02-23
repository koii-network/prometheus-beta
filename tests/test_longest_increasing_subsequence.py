import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_length():
    """Test basic length calculation of LIS"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr) == 6

def test_basic_sequence():
    """Test returning the actual LIS"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 50, 60, 80]

def test_ascending_array():
    """Test fully ascending array"""
    arr = [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_sequence=True) == [1, 2, 3, 4, 5]

def test_descending_array():
    """Test fully descending array"""
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_single_element_array():
    """Test array with single element"""
    arr = [42]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [42]

def test_empty_array_error():
    """Test that empty array raises ValueError"""
    with pytest.raises(ValueError):
        longest_increasing_subsequence([])

def test_non_list_input_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")

def test_duplicate_elements():
    """Test array with duplicate elements"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_increasing_subsequence(arr) == 6
    assert longest_increasing_subsequence(arr, return_sequence=True) == [0, 2, 6, 9, 13, 15]
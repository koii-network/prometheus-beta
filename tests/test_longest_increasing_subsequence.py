import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    arr = [10, 22, 33, 44, 55]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 44, 55]

def test_non_consecutive_increasing_sequence():
    """Test a non-consecutive increasing subsequence"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_single_element_sequence():
    """Test a single element sequence"""
    arr = [5]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_repeated_elements_sequence():
    """Test a sequence with repeated elements"""
    arr = [7, 7, 7, 7, 7, 7, 7]
    assert find_longest_increasing_subsequence(arr) == [7]

def test_unsorted_input():
    """Test an unsorted input sequence"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 4, 5, 6]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_increasing_subsequence([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_longest_increasing_subsequence("not a list")
        find_longest_increasing_subsequence(123)
        find_longest_increasing_subsequence(None)
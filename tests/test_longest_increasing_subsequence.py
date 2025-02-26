import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_empty_list():
    """Test empty list returns 0 length or empty subsequence"""
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([], return_sequence=True) == []

def test_single_element():
    """Test list with single element"""
    assert longest_increasing_subsequence([5]) == 1
    assert longest_increasing_subsequence([5], return_sequence=True) == [5]

def test_basic_increasing_sequence():
    """Test basic increasing sequence"""
    arr = [10, 22, 33, 44, 55]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 44, 55]

def test_non_consecutive_increasing_sequence():
    """Test non-consecutive increasing sequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr) == 6
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 50, 60, 80]

def test_unsorted_input():
    """Test unsorted input with multiple possible subsequences"""
    arr = [3, 10, 2, 1, 20]
    assert longest_increasing_subsequence(arr) == 3
    assert (longest_increasing_subsequence(arr, return_sequence=True) == [3, 10, 20] or 
            longest_increasing_subsequence(arr, return_sequence=True) == [1, 2, 20])

def test_descending_input():
    """Test input with descending order"""
    arr = [7, 6, 5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1
    assert len(longest_increasing_subsequence(arr, return_sequence=True)) == 1

def test_float_input():
    """Test input with float values"""
    arr = [1.5, 2.3, 3.7, 4.2, 5.1]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_sequence=True) == [1.5, 2.3, 3.7, 4.2, 5.1]

def test_input_validation():
    """Test input validation"""
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")
    
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, "string"])
    
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, None])
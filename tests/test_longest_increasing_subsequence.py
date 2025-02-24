import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_typical_case_length():
    """Test typical case returning length"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert longest_increasing_subsequence(arr) == 5

def test_typical_case_sequence():
    """Test typical case returning sequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 50, 60]

def test_empty_list_length():
    """Test empty list returns 0 for length"""
    assert longest_increasing_subsequence([]) == 0

def test_empty_list_sequence():
    """Test empty list returns empty list for sequence"""
    assert longest_increasing_subsequence([], return_sequence=True) == []

def test_single_element_length():
    """Test single element list returns 1 for length"""
    assert longest_increasing_subsequence([5]) == 1

def test_single_element_sequence():
    """Test single element list returns the element for sequence"""
    assert longest_increasing_subsequence([5], return_sequence=True) == [5]

def test_descending_list_length():
    """Test descending list returns 1 for length"""
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1

def test_descending_list_sequence():
    """Test descending list returns single element for sequence"""
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr, return_sequence=True) == [1]

def test_all_same_elements_length():
    """Test list with all same elements returns 1 for length"""
    arr = [2, 2, 2, 2, 2]
    assert longest_increasing_subsequence(arr) == 1

def test_all_same_elements_sequence():
    """Test list with all same elements returns single element for sequence"""
    arr = [2, 2, 2, 2, 2]
    assert longest_increasing_subsequence(arr, return_sequence=True) == [2]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test that ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        longest_increasing_subsequence([1, 2, "3", 4])

def test_multiple_possible_subsequences():
    """Test case with multiple possible longest increasing subsequences"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_increasing_subsequence(arr) == 6
    assert longest_increasing_subsequence(arr, return_sequence=True) in [
        [0, 2, 6, 9, 13, 15],
        [0, 2, 6, 10, 13, 15],
        [0, 4, 6, 9, 13, 15],
        [0, 4, 6, 10, 13, 15],
        [0, 2, 6, 9, 11, 15],
        # Add more valid subsequences if needed
    ]
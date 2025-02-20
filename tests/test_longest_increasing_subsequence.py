import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_length():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr) == 6

def test_basic_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 50, 60, 80]

def test_single_element():
    arr = [5]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_sorted_ascending():
    arr = [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_sequence=True) == [1, 2, 3, 4, 5]

def test_sorted_descending():
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_invalid_input_empty():
    with pytest.raises(ValueError):
        longest_increasing_subsequence([])

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        longest_increasing_subsequence(123)

def test_duplicate_elements():
    arr = [1, 2, 2, 3, 4, 4, 5]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_sequence=True) == [1, 2, 3, 4, 5]
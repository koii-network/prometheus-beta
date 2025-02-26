import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_length_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr) == 6
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 50, 60, 80]

def test_empty_list():
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([], return_sequence=True) == []

def test_single_element():
    arr = [5]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_all_same_elements():
    arr = [2, 2, 2, 2, 2]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [2]

def test_multiple_equal_length_sequences():
    arr = [1, 2, 3, 2, 3, 4]
    assert longest_increasing_subsequence(arr) == 4
    assert longest_increasing_subsequence(arr, return_sequence=True) == [1, 2, 3, 4]

def test_invalid_input_types():
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")
    with pytest.raises(TypeError):
        longest_increasing_subsequence(None)

def test_non_numeric_elements():
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, "three"])
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, None])
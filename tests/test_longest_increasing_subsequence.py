import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_normal_increasing_sequence():
    arr = [10, 22, 33, 44, 55]
    assert longest_increasing_subsequence(arr) == 5

def test_non_continuous_increasing_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert longest_increasing_subsequence(arr) == 5

def test_all_same_numbers():
    arr = [5, 5, 5, 5, 5]
    assert longest_increasing_subsequence(arr) == 1

def test_unsorted_array():
    arr = [7, 7, 7, 7, 7, 7, 7]
    assert longest_increasing_subsequence(arr) == 1

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1

def test_empty_list():
    arr = []
    assert longest_increasing_subsequence(arr) == 0

def test_single_element():
    arr = [42]
    assert longest_increasing_subsequence(arr) == 1

def test_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        longest_increasing_subsequence(42)

def test_invalid_input_non_integers():
    with pytest.raises(ValueError, match="List must contain only integers"):
        longest_increasing_subsequence([1, 2, 'a', 3])
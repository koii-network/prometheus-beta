import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    arr = [10, 22, 33, 44]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 44]

def test_non_consecutive_increasing_sequence():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_sequence_with_duplicates():
    arr = [2, 5, 1, 8, 3, 5, 4, 7]
    assert find_longest_increasing_subsequence(arr) == [1, 3, 5, 7]

def test_single_element_sequence():
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_empty_input():
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([])
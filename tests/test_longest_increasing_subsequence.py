import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_increasing_sequence():
    arr = [10, 22, 33, 44, 55]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 44, 55]

def test_non_consecutive_increasing_sequence():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_empty_list():
    assert find_longest_increasing_subsequence([]) == []

def test_single_element_list():
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]

def test_all_same_elements():
    arr = [5, 5, 5, 5, 5]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_unsorted_list():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 4, 5, 6]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_decreasing_sequence():
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]
import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_increasing_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 50, 60]

def test_sorted_sequence():
    arr = [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2, 3, 4, 5]

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_empty_list():
    arr = []
    assert find_longest_increasing_subsequence(arr) == []

def test_single_element():
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]

def test_duplicate_values():
    arr = [2, 2, 2, 2, 2]
    assert find_longest_increasing_subsequence(arr) == [2]

def test_multiple_increasing_subsequences():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_invalid_input_non_numeric():
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        find_longest_increasing_subsequence([1, 2, "three", 4])

def test_mixed_numeric_types():
    arr = [1, 2.5, 3, 4.7, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2.5, 3, 4.7, 5]
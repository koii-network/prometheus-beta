import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60, 80]

def test_empty_list():
    arr = []
    result = find_longest_increasing_subsequence(arr)
    assert result == []

def test_single_element():
    arr = [5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5]

def test_descending_array():
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5] or result == [4] or result == [3] or result == [2] or result == [1]

def test_all_equal_elements():
    arr = [2, 2, 2, 2, 2]
    result = find_longest_increasing_subsequence(arr)
    assert result == [2]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_multiple_same_length_subsequences():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    assert result == [0, 2, 6, 9, 13, 15]
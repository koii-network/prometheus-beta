import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    arr = [10, 22, 33, 44, 55]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 44, 55]

def test_mixed_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60]

def test_single_element():
    arr = [5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5]

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5] or result == [4] or result == [3] or result == [2] or result == [1]

def test_duplicate_elements():
    arr = [2, 2, 2, 3, 3, 4, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [2, 3, 4]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_empty_list():
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([])
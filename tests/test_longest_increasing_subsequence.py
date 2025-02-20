import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60, 80], "Should find the longest increasing subsequence"

def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3, 4, 5], "Should return the entire sorted array"

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5], "Should return single element when no increasing subsequence"

def test_single_element():
    arr = [42]
    result = find_longest_increasing_subsequence(arr)
    assert result == [42], "Should return single element array"

def test_multiple_possible_subsequences():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    assert result == [0, 2, 6, 9, 13, 15], "Should handle complex sequence with multiple possible subsequences"

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_longest_increasing_subsequence("not a list")

def test_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_increasing_subsequence([])
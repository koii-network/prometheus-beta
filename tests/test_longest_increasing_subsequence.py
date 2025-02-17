import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60]

def test_strictly_increasing_array():
    arr = [1, 2, 3, 4, 5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3, 4, 5]

def test_decreasing_array():
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5]

def test_empty_array():
    arr = []
    result = find_longest_increasing_subsequence(arr)
    assert result == []

def test_single_element_array():
    arr = [42]
    result = find_longest_increasing_subsequence(arr)
    assert result == [42]

def test_multiple_equal_length_subsequences():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    # Verify it is a valid longest increasing subsequence
    assert len(result) == 6  # Known maximum length
    assert len(set(result)) == len(result)  # No duplicates
    for i in range(len(result)-1):
        assert result[i] < result[i+1], f"Not strictly increasing: {result}"

def test_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_invalid_input_non_numeric():
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        find_longest_increasing_subsequence([1, 2, "three"])

def test_float_input():
    arr = [1.5, 2.3, 0.8, 3.7, 2.1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1.5, 2.3, 3.7]
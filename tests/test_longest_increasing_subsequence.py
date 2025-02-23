import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_sequence():
    """Test a standard increasing sequence."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60, 80]

def test_empty_list():
    """Test handling of an empty list."""
    arr = []
    result = find_longest_increasing_subsequence(arr)
    assert result == []

def test_single_element():
    """Test a list with a single element."""
    arr = [5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5]

def test_already_sorted_list():
    """Test a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3, 4, 5]

def test_decreasing_list():
    """Test a list that is in descending order."""
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5] or result == [4] or result == [3] or result == [2] or result == [1]

def test_duplicate_elements():
    """Test a list with duplicate elements."""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    # There can be multiple valid LIS for this input
    valid_subsequences = [
        [0, 2, 6, 9, 13, 15],
        [0, 4, 6, 9, 13, 15],
        [0, 2, 6, 10, 13, 15],
        [0, 4, 6, 10, 13, 15]
    ]
    assert result in valid_subsequences

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_uncomparable_elements():
    """Test that a ValueError is raised for uncomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        find_longest_increasing_subsequence([1, '2', 3])

def test_mixed_type_elements():
    """Test mixed type elements that cannot be compared."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        find_longest_increasing_subsequence([1, 2, 'a', 3, 4])
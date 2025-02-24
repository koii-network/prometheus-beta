import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    arr = [10, 22, 33, 44, 55]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 44, 55]

def test_non_consecutive_increasing_sequence():
    """Test a non-consecutive increasing sequence"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_empty_list():
    """Test empty list returns empty list"""
    assert find_longest_increasing_subsequence([]) == []

def test_single_element():
    """Test list with a single element"""
    assert find_longest_increasing_subsequence([5]) == [5]

def test_duplicate_elements():
    """Test list with duplicate elements"""
    arr = [5, 5, 5, 5, 5]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_decreasing_sequence():
    """Test a strictly decreasing sequence"""
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_mixed_sequence():
    """Test a mixed sequence with multiple subsequence possibilities"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 4, 5, 6]

def test_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_value_error():
    """Test that ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        find_longest_increasing_subsequence([1, 2, "three", 4])

def test_floating_point_numbers():
    """Test works with floating point numbers"""
    arr = [1.1, 2.2, 1.5, 3.3, 4.4]
    assert find_longest_increasing_subsequence(arr) == [1.1, 2.2, 3.3, 4.4]
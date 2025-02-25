import pytest
from src.longest_consecutive_sequence import find_longest_consecutive_sequence

def test_basic_consecutive_sequence():
    """Test basic consecutive sequence detection"""
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_longer_consecutive_sequence():
    """Test longer consecutive sequence"""
    assert find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_empty_list():
    """Test empty list input"""
    assert find_longest_consecutive_sequence([]) == []

def test_single_element():
    """Test list with single element"""
    assert find_longest_consecutive_sequence([5]) == [5]

def test_duplicate_numbers():
    """Test list with duplicate numbers"""
    assert find_longest_consecutive_sequence([1, 1, 2, 2, 3, 3]) == [1, 2, 3]

def test_unsorted_list():
    """Test unsorted list with non-consecutive numbers"""
    assert find_longest_consecutive_sequence([9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]) == [-4, -3, -2, -1]

def test_no_consecutive_sequence():
    """Test list with no consecutive sequence"""
    assert find_longest_consecutive_sequence([5, 10, 15, 20]) == [5]
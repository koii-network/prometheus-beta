import pytest
from src.most_frequent_integer import find_most_frequent_integer_index

def test_basic_frequency():
    """Test basic frequency finding"""
    assert find_most_frequent_integer_index([1, 2, 2, 3, 3, 3]) == 3

def test_tie_breaking():
    """Test that the first occurrence is returned in case of a tie"""
    assert find_most_frequent_integer_index([1, 1, 2, 2]) == 0

def test_single_element():
    """Test list with a single element"""
    assert find_most_frequent_integer_index([5]) == 0

def test_all_unique():
    """Test list with all unique elements"""
    assert find_most_frequent_integer_index([1, 2, 3, 4, 5]) == 0

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_most_frequent_integer_index([])

def test_negative_numbers():
    """Test with negative numbers"""
    assert find_most_frequent_integer_index([-1, -1, -2, -2, -3]) == 0

def test_mixed_frequency():
    """Test with mixed frequency of numbers"""
    assert find_most_frequent_integer_index([1, 2, 2, 3, 1, 1, 4]) == 0
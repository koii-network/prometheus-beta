import pytest
from src.most_frequent_index import find_most_frequent_index

def test_basic_most_frequent():
    """Test basic scenario with a clear most frequent element"""
    assert find_most_frequent_index([1, 2, 2, 3, 3, 3]) == 3

def test_first_occurrence_in_tie():
    """Test that the first occurrence is returned in case of a tie"""
    assert find_most_frequent_index([1, 2, 2, 1, 3, 3]) == 0

def test_single_element_list():
    """Test list with a single element"""
    assert find_most_frequent_index([5]) == 0

def test_all_unique_elements():
    """Test list where all elements have the same frequency"""
    assert find_most_frequent_index([1, 2, 3]) == 0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError):
        find_most_frequent_index([])
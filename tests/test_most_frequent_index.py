import pytest
from src.most_frequent_index import find_most_frequent_index

def test_basic_most_frequent():
    """Test basic case with a clear most frequent number"""
    assert find_most_frequent_index([1, 2, 2, 3, 3, 3, 4]) == 3

def test_first_occurrence_in_tie():
    """Test that first occurrence is returned in case of a frequency tie"""
    assert find_most_frequent_index([1, 2, 2, 1, 3, 3]) == 1

def test_single_element_list():
    """Test list with a single element"""
    assert find_most_frequent_index([5]) == 0

def test_all_elements_same():
    """Test list where all elements are the same"""
    assert find_most_frequent_index([1, 1, 1, 1]) == 0

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        find_most_frequent_index([])
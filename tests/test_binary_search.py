import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from binary_search import binary_search

def test_binary_search_basic():
    """Test basic functionality of binary search"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 15) == 7
    assert binary_search(arr, 1) == 0

def test_binary_search_not_found():
    """Test when target is not in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 16) == -1
    assert binary_search(arr, 6) == -1

def test_binary_search_edge_cases():
    """Test edge cases like empty list, single element list"""
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1

def test_binary_search_invalid_input():
    """Test input validation"""
    # Test non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)
    
    # Test unsorted list
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1], 3)

def test_binary_search_duplicates():
    """Test binary search with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    # Returns the index of first occurrence of target
    assert binary_search(arr, 3) in [3, 4, 5]
    assert binary_search(arr, 2) in [1, 2]
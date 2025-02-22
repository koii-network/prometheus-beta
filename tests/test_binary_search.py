import pytest
from src.binary_search import binary_search

def test_binary_search_normal_case():
    """Test binary search with a typical sorted array."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 13) == 6

def test_binary_search_edge_cases():
    """Test binary search with edge cases."""
    # Empty array
    assert binary_search([], 5) == -1
    
    # Single element arrays
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1
    
    # First and last elements
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 15) == 7

def test_binary_search_not_found():
    """Test when target is not in the array."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 16) == -1
    assert binary_search(arr, 6) == -1

def test_binary_search_large_array():
    """Test binary search with a large sorted array."""
    arr = list(range(0, 1000, 2))  # Even numbers from 0 to 998
    assert binary_search(arr, 500) == 250
    assert binary_search(arr, 501) == -1
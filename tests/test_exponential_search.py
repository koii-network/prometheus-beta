import pytest
from src.exponential_search import exponential_search

def test_exponential_search_found():
    """Test finding an element that exists in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 3
    assert exponential_search(arr, 1) == 0
    assert exponential_search(arr, 15) == 7

def test_exponential_search_not_found():
    """Test searching for an element not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 0) == -1
    assert exponential_search(arr, 16) == -1
    assert exponential_search(arr, 6) == -1

def test_exponential_search_edge_cases():
    """Test edge cases"""
    # Single element list
    assert exponential_search([5], 5) == 0
    assert exponential_search([5], 6) == -1
    
    # Large lists
    large_arr = list(range(0, 1000, 2))
    assert exponential_search(large_arr, 500) == 250

def test_exponential_search_error_cases():
    """Test error handling"""
    # Empty list
    with pytest.raises(ValueError, match="Cannot search in an empty list"):
        exponential_search([], 5)
    
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        exponential_search("not a list", 5)
        
    with pytest.raises(TypeError, match="Input must be a list"):
        exponential_search(123, 5)
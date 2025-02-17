import pytest
from src.exponential_search import exponential_search

def test_exponential_search_basic():
    """Test basic functionality of exponential search"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 3
    assert exponential_search(arr, 1) == 0
    assert exponential_search(arr, 15) == 7

def test_exponential_search_not_found():
    """Test when element is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 4) == -1
    assert exponential_search(arr, 16) == -1

def test_exponential_search_edge_cases():
    """Test edge cases"""
    # Single element list
    assert exponential_search([5], 5) == 0
    assert exponential_search([5], 6) == -1

def test_exponential_search_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(TypeError):
        exponential_search("not a list", 5)
    
    with pytest.raises(ValueError):
        exponential_search([], 5)

def test_exponential_search_large_list():
    """Test with a larger sorted list"""
    arr = list(range(0, 1000, 2))  # Even numbers from 0 to 998
    assert exponential_search(arr, 500) == arr.index(500)
    assert exponential_search(arr, 501) == -1
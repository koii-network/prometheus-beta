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

def test_exponential_search_single_element():
    """Test search in a single-element list"""
    arr = [5]
    assert exponential_search(arr, 5) == 0
    assert exponential_search(arr, 6) == -1

def test_exponential_search_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        exponential_search("not a list", 5)
    
    with pytest.raises(ValueError):
        exponential_search([], 5)

def test_exponential_search_large_list():
    """Test exponential search on a larger sorted list"""
    arr = list(range(0, 1000, 2))  # Even numbers from 0 to 998
    assert exponential_search(arr, 500) == arr.index(500)
    assert exponential_search(arr, 501) == -1
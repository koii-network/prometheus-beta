import pytest
from src.exponential_search import exponential_search

def test_normal_search():
    """Test searching for an element in the middle of a sorted list."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 3
    assert exponential_search(arr, 15) == 7
    assert exponential_search(arr, 1) == 0

def test_not_found():
    """Test searching for elements not in the list."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 0) == -1
    assert exponential_search(arr, 16) == -1
    assert exponential_search(arr, 6) == -1

def test_single_element():
    """Test searching in a single-element list."""
    arr = [5]
    assert exponential_search(arr, 5) == 0
    assert exponential_search(arr, 6) == -1

def test_edge_cases():
    """Test various edge cases."""
    # First element
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 1) == 0
    
    # Last element
    assert exponential_search(arr, 15) == 7

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Empty list
    with pytest.raises(ValueError, match="Cannot search in an empty list"):
        exponential_search([], 5)
    
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        exponential_search("not a list", 5)

def test_large_list():
    """Test exponential search on a larger sorted list."""
    arr = list(range(0, 1000, 2))  # Even numbers from 0 to 998
    assert exponential_search(arr, 500) == arr.index(500)
    assert exponential_search(arr, 501) == -1

def test_duplicate_elements():
    """Test searching with duplicate elements."""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    assert exponential_search(arr, 3) in [3, 4, 5]  # Any index of 3 is acceptable
import pytest
from src.linear_search import linear_search

def test_linear_search_basic():
    """Test basic functionality of linear search."""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 3) == 2
    assert linear_search(arr, 5) == 4

def test_linear_search_first_element():
    """Test when target is the first element."""
    arr = [10, 20, 30, 40, 50]
    assert linear_search(arr, 10) == 0

def test_linear_search_last_element():
    """Test when target is the last element."""
    arr = [10, 20, 30, 40, 50]
    assert linear_search(arr, 50) == 4

def test_linear_search_not_found():
    """Test when target is not in the list."""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 6) == -1

def test_linear_search_empty_list():
    """Test searching in an empty list."""
    arr = []
    assert linear_search(arr, 10) == -1

def test_linear_search_multiple_occurrences():
    """Test when target appears multiple times."""
    arr = [1, 2, 3, 2, 4, 2]
    assert linear_search(arr, 2) == 1  # Returns index of first occurrence

def test_linear_search_different_types():
    """Test searching with different types of elements."""
    arr = [1, 'a', True, 3.14, None]
    assert linear_search(arr, 'a') == 1
    assert linear_search(arr, True) == 0  # True is at index 0, not 2
    assert linear_search(arr, 3.14) == 3
    assert linear_search(arr, None) == 4

def test_linear_search_invalid_input():
    """Test error handling for invalid input."""
    with pytest.raises(TypeError):
        linear_search("not a list", 5)
    with pytest.raises(TypeError):
        linear_search(123, 5)
    with pytest.raises(TypeError):
        linear_search(None, 5)
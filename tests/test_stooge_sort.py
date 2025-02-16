import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_basic():
    """Test basic sorting functionality"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert stooge_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_stooge_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert stooge_sort(arr) == []

def test_stooge_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert stooge_sort(arr) == [42]

def test_stooge_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert stooge_sort(arr) == [1, 2, 3, 4, 5]

def test_stooge_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert stooge_sort(arr) == [1, 2, 3, 4, 5]

def test_stooge_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert stooge_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_stooge_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        stooge_sort("not a list")
    with pytest.raises(TypeError):
        stooge_sort(123)
    with pytest.raises(TypeError):
        stooge_sort(None)
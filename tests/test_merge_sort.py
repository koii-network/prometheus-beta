import pytest
from src.merge_sort import merge_sort

def test_merge_sort_basic():
    """Test basic sorting of integers."""
    arr = [5, 2, 9, 1, 7, 6]
    result = merge_sort(arr)
    assert result == [1, 2, 5, 6, 7, 9]
    assert arr != result  # Ensure original list is not modified

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    result = merge_sort(arr)
    assert result == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    result = merge_sort(arr)
    assert result == [42]

def test_merge_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    result = merge_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    result = merge_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_merge_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = merge_sort(arr)
    assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_merge_sort_floating_point():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 1.41, 2.71, 0.58]
    result = merge_sort(arr)
    assert result == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        merge_sort("not a list")
    
    with pytest.raises(TypeError):
        merge_sort(42)
    
    with pytest.raises(TypeError):
        merge_sort(None)
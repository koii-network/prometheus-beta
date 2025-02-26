import pytest
from src.bubble_sort import bubble_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert bubble_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert bubble_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert bubble_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubble_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 2, -3, 0, 1, -1]
    assert bubble_sort(input_list) == [-5, -3, -1, 0, 1, 2]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort(None)
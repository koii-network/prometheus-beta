import pytest
from src.insertion_sort import insertion_sort

def test_insertion_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert insertion_sort(input_list) == expected

def test_insertion_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == input_list

def test_insertion_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == expected

def test_insertion_sort_empty_list():
    """Test sorting an empty list."""
    assert insertion_sort([]) == []

def test_insertion_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert insertion_sort(input_list) == input_list

def test_insertion_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert insertion_sort(input_list) == expected

def test_insertion_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort(None)
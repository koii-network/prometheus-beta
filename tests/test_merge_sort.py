import pytest
from src.merge_sort import merge_sort

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    assert merge_sort([42]) == [42]

def test_merge_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted_list():
    """Test sorting an unsorted list."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_merge_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert merge_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_merge_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 0, 3, -2, 7, -1]
    assert merge_sort(input_list) == [-5, -2, -1, 0, 3, 7]

def test_merge_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort(None)
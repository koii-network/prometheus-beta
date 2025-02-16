import pytest
from src.selection_sort import selection_sort

def test_selection_sort_normal_list():
    """Test sorting a list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert selection_sort(input_list) == expected

def test_selection_sort_empty_list():
    """Test sorting an empty list."""
    assert selection_sort([]) == []

def test_selection_sort_single_element():
    """Test sorting a list with a single element."""
    assert selection_sort([5]) == [5]

def test_selection_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == input_list

def test_selection_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert selection_sort(input_list) == expected

def test_selection_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert selection_sort(input_list) == expected

def test_selection_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 0, 7, -1]
    expected = sorted(input_list)
    assert selection_sort(input_list) == expected

def test_selection_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")

def test_selection_sort_uncomparable_elements():
    """Test that ValueError is raised for list with uncomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        selection_sort([1, 2, "a"])

def test_selection_sort_preserves_original_list():
    """Test that the original list is not modified."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    original_copy = input_list.copy()
    selection_sort(input_list)
    assert input_list == original_copy
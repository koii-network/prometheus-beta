import pytest
from src.selection_sort import selection_sort

def test_selection_sort_normal_list():
    """Test sorting a list of integers."""
    input_list = [64, 25, 12, 22, 11]
    expected = [11, 12, 22, 25, 64]
    assert selection_sort(input_list) == expected

def test_selection_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == input_list

def test_selection_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected

def test_selection_sort_empty_list():
    """Test sorting an empty list."""
    assert selection_sort([]) == []

def test_selection_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert selection_sort(input_list) == input_list

def test_selection_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert selection_sort(input_list) == expected

def test_selection_sort_float_numbers():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 1.41, 2.71, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert selection_sort(input_list) == expected

def test_selection_sort_invalid_input():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")

def test_selection_sort_non_comparable():
    """Test raising ValueError for non-comparable elements."""
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        selection_sort([1, 2, "3", 4])
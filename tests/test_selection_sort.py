import pytest
from src.selection_sort import selection_sort

def test_selection_sort_positive_numbers():
    """Test sorting a list of positive numbers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert selection_sort(input_list) == expected

def test_selection_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, -10, -3, -1, -8]
    expected = [-10, -8, -5, -3, -1]
    assert selection_sort(input_list) == expected

def test_selection_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    input_list = [5, -2, 0, 10, -7, 3]
    expected = [-7, -2, 0, 3, 5, 10]
    assert selection_sort(input_list) == expected

def test_selection_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected

def test_selection_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected

def test_selection_sort_duplicate_numbers():
    """Test sorting a list with duplicate numbers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert selection_sort(input_list) == expected

def test_selection_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    expected = []
    assert selection_sort(input_list) == expected

def test_selection_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    expected = [42]
    assert selection_sort(input_list) == expected

def test_selection_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")

def test_selection_sort_uncomparable_elements():
    """Test that ValueError is raised for incomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        selection_sort([1, "a", 3])
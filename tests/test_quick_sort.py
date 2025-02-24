import pytest
from src.quick_sort import quick_sort

def test_quick_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [3, 6, 8, 10, 1, 2, 1]
    expected = [1, 1, 2, 3, 6, 8, 10]
    assert quick_sort(input_list) == expected

def test_quick_sort_empty_list():
    """Test sorting an empty list."""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test sorting a list with a single element."""
    assert quick_sort([42]) == [42]

def test_quick_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == input_list

def test_quick_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == expected

def test_quick_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 3, 3, 1, 1, 2]
    expected = [1, 1, 2, 3, 3, 3]
    assert quick_sort(input_list) == expected

def test_quick_sort_float_list():
    """Test sorting a list of floats."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert quick_sort(input_list) == expected

def test_quick_sort_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort(123)

def test_quick_sort_incomparable_types():
    """Test that a TypeError is raised for incomparable types."""
    with pytest.raises(TypeError, match="List contains elements of incomparable types"):
        quick_sort([1, "string", 3])

def test_quick_sort_original_list_unchanged():
    """Test that the original list remains unchanged."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    original_copy = input_list.copy()
    quick_sort(input_list)
    assert input_list == original_copy
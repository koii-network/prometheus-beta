import pytest
from src.quick_sort import quick_sort

def test_quick_sort_normal_list():
    """Test sorting a list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
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
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_with_strings():
    """Test sorting a list of strings."""
    input_list = ["banana", "apple", "cherry", "date"]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_does_not_modify_original():
    """Test that the original list is not modified."""
    input_list = [3, 1, 4, 1, 5]
    original_copy = input_list.copy()
    quick_sort(input_list)
    assert input_list == original_copy

def test_quick_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")

def test_quick_sort_non_comparable_elements():
    """Test handling of non-comparable elements."""
    with pytest.raises(TypeError, match="List contains non-comparable elements"):
        quick_sort([1, 2, [3], 4])  # List cannot be compared
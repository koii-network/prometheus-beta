import pytest
from src.selection_sort import selection_sort

def test_selection_sort_numbers():
    """Test sorting a list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert selection_sort(input_list) == expected

def test_selection_sort_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert selection_sort(input_list) == expected

def test_selection_sort_empty_list():
    """Test sorting an empty list."""
    assert selection_sort([]) == []

def test_selection_sort_single_element():
    """Test sorting a list with a single element."""
    assert selection_sort([42]) == [42]

def test_selection_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == input_list

def test_selection_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected

def test_selection_sort_strings():
    """Test sorting a list of strings."""
    input_list = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    assert selection_sort(input_list) == expected

def test_selection_sort_input_not_list():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")
        selection_sort(123)
        selection_sort(None)

def test_selection_sort_uncomparable_elements():
    """Test that a ValueError is raised for lists with uncomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        selection_sort([1, 2, "three"])
        selection_sort([1, None, 3])
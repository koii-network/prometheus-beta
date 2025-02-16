import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_integer_list():
    """Test sorting a list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected_output = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(input_list) == expected_output

def test_bubble_sort_float_list():
    """Test sorting a list of floats."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected_output = [0.58, 1.41, 2.71, 3.14]
    assert bubble_sort(input_list) == expected_output

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element_list():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert bubble_sort(input_list) == [42]

def test_bubble_sort_already_sorted_list():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected_output

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort(input_list) == expected_output

def test_bubble_sort_invalid_input_type():
    """Test that a TypeError is raised when input is not a list."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")

def test_bubble_sort_uncomparable_elements():
    """Test that a ValueError is raised when list contains uncomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        bubble_sort([1, 2, "three"])
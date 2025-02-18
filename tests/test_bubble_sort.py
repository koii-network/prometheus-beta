import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_numeric_list():
    """Test sorting a list of numbers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element."""
    assert bubble_sort([42]) == [42]

def test_bubble_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_string_list():
    """Test sorting a list of strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = ['apple', 'banana', 'cherry', 'date']
    assert bubble_sort(input_list) == expected

def test_bubble_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort(123)

def test_bubble_sort_incomparable_elements():
    """Test that a ValueError is raised for incomparable elements."""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        bubble_sort([1, 2, '3', 4])
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        bubble_sort([(1,2), (3,4), 5])
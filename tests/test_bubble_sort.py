import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_normal_list():
    """Test bubble sort with a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_already_sorted():
    """Test bubble sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == input_list

def test_bubble_sort_reverse_sorted():
    """Test bubble sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_with_duplicates():
    """Test bubble sort with a list containing duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_empty_list():
    """Test bubble sort with an empty list."""
    input_list = []
    assert bubble_sort(input_list) == []

def test_bubble_sort_single_element():
    """Test bubble sort with a single-element list."""
    input_list = [42]
    assert bubble_sort(input_list) == [42]

def test_bubble_sort_float_list():
    """Test bubble sort with a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_negative_numbers():
    """Test bubble sort with a list containing negative numbers."""
    input_list = [-5, 3, -2, 0, 7, -1]
    expected = sorted(input_list)
    assert bubble_sort(input_list) == expected

def test_bubble_sort_invalid_input_type():
    """Test bubble sort with an invalid input type."""
    with pytest.raises(TypeError):
        bubble_sort("not a list")

def test_bubble_sort_uncomparable_elements():
    """Test bubble sort with elements that cannot be compared."""
    with pytest.raises(ValueError):
        bubble_sort([1, 2, "3", 4])
import pytest
from src.quick_sort import quick_sort

def test_quick_sort_normal_list():
    """Test Quick Sort with a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected_output = [11, 12, 22, 25, 34, 64, 90]
    assert quick_sort(input_list) == expected_output

def test_quick_sort_already_sorted():
    """Test Quick Sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == input_list

def test_quick_sort_reverse_sorted():
    """Test Quick Sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == expected_output

def test_quick_sort_empty_list():
    """Test Quick Sort with an empty list."""
    input_list = []
    assert quick_sort(input_list) == []

def test_quick_sort_single_element():
    """Test Quick Sort with a single-element list."""
    input_list = [42]
    assert quick_sort(input_list) == [42]

def test_quick_sort_with_duplicates():
    """Test Quick Sort with a list containing duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert quick_sort(input_list) == expected_output

def test_quick_sort_negative_numbers():
    """Test Quick Sort with negative numbers."""
    input_list = [-5, 2, -3, 0, 7, -1]
    expected_output = [-5, -3, -1, 0, 2, 7]
    assert quick_sort(input_list) == expected_output

def test_quick_sort_invalid_input_type():
    """Test Quick Sort with an invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort(123)
import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_normal_list():
    """Test sorting a standard list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert pancake_sort(input_list) == input_list

def test_pancake_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    assert pancake_sort(input_list) == []

def test_pancake_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert pancake_sort(input_list) == [42]

def test_pancake_sort_with_float_numbers():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        pancake_sort("not a list")

def test_pancake_sort_non_comparable_elements():
    """Test that a ValueError is raised for non-comparable elements."""
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        pancake_sort([1, 2, "3", 4])
import pytest
from src.insertion_sort import insertion_sort

def test_basic_sorting():
    """Test sorting a simple list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert insertion_sort(input_list) == expected

def test_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == input_list

def test_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list."""
    assert insertion_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element."""
    assert insertion_sort([42]) == [42]

def test_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [4, 2, 4, 1, 3, 2]
    expected = [1, 2, 2, 3, 4, 4]
    assert insertion_sort(input_list) == expected

def test_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-4, 2, -1, 0, 3, -2]
    expected = [-4, -2, -1, 0, 2, 3]
    assert insertion_sort(input_list) == expected

def test_float_numbers():
    """Test sorting a list with floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert insertion_sort(input_list) == expected

def test_input_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")
        insertion_sort(123)
        insertion_sort(None)
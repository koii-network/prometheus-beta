import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test sorting a basic list of integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_single_element_list():
    """Test sorting a list with a single element"""
    arr = [5]
    assert counting_sort(arr) == [5]

def test_list_with_repeated_elements():
    """Test sorting a list with multiple repeated elements"""
    arr = [3, 3, 3, 3, 3]
    assert counting_sort(arr) == [3, 3, 3, 3, 3]

def test_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_non_integer_elements():
    """Test handling of non-integer list elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, 'a', 3])

def test_negative_numbers():
    """Test handling of negative numbers"""
    with pytest.raises(ValueError, match="Input must contain only non-negative integers"):
        counting_sort([1, 2, -3, 4])

def test_large_range_of_numbers():
    """Test sorting a list with a large range of numbers"""
    arr = [10000, 5, 1000, 100, 0, 50, 10000]
    assert counting_sort(arr) == [0, 5, 50, 100, 1000, 10000, 10000]
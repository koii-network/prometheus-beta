import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting of a list of non-negative integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_all_same_elements():
    """Test sorting a list with all same elements"""
    arr = [3, 3, 3, 3, 3]
    assert counting_sort(arr) == [3, 3, 3, 3, 3]

def test_zero_included():
    """Test sorting a list that includes zero"""
    arr = [0, 5, 2, 0, 1, 3]
    assert counting_sort(arr) == [0, 0, 1, 2, 3, 5]

def test_invalid_input_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError):
        counting_sort("not a list")

def test_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, -3, 4])

def test_non_integer_elements():
    """Test that non-integer elements raise a ValueError"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, 3.5, 4])
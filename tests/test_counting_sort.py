import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic functionality of counting sort"""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted():
    """Test sorting a list that is already sorted"""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_same_elements():
    """Test sorting a list with all identical elements"""
    assert counting_sort([3, 3, 3, 3]) == [3, 3, 3, 3]

def test_zero_included():
    """Test sorting a list that includes zero"""
    assert counting_sort([0, 3, 1, 0, 2]) == [0, 0, 1, 2, 3]

def test_invalid_input_negative():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError):
        counting_sort([4, -1, 2])

def test_invalid_input_non_integer():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError):
        counting_sort([1, 2, 'a'])

def test_invalid_input_non_list():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        counting_sort("not a list")
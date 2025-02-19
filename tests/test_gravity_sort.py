import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_basic():
    """Test basic sorting functionality"""
    assert gravity_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_gravity_sort_empty_list():
    """Test sorting an empty list"""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test sorting a list with a single element"""
    assert gravity_sort([42]) == [42]

def test_gravity_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert gravity_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_gravity_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert gravity_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_gravity_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    assert gravity_sort([3, 3, 1, 1, 4, 4, 2, 2]) == [1, 1, 2, 2, 3, 3, 4, 4]

def test_gravity_sort_zero_values():
    """Test sorting a list with zero values"""
    assert gravity_sort([0, 0, 3, 0, 1]) == [0, 0, 0, 1, 3]

def test_gravity_sort_negative_input_error():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        gravity_sort([-1, 2, 3])

def test_gravity_sort_non_integer_input_error():
    """Test that non-integer input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        gravity_sort([1, 2, 'a'])
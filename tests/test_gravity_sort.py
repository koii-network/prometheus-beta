import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_basic():
    """Test basic sorting functionality"""
    input_arr = [5, 3, 2, 7, 1]
    expected = [1, 2, 3, 5, 7]
    assert gravity_sort(input_arr) == expected

def test_gravity_sort_already_sorted():
    """Test when input is already sorted"""
    input_arr = [1, 2, 3, 4, 5]
    assert gravity_sort(input_arr) == input_arr

def test_gravity_sort_reverse_sorted():
    """Test sorting a reverse-sorted array"""
    input_arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_arr) == expected

def test_gravity_sort_with_duplicates():
    """Test sorting an array with duplicate values"""
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    assert gravity_sort(input_arr) == expected

def test_gravity_sort_empty_list():
    """Test sorting an empty list"""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test sorting a list with a single element"""
    input_arr = [42]
    assert gravity_sort(input_arr) == [42]

def test_gravity_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Gravity sort only works with non-negative integers"):
        gravity_sort([-1, 2, 3])

def test_gravity_sort_zero_values():
    """Test sorting a list with zero values"""
    input_arr = [0, 5, 0, 3, 0]
    expected = [0, 0, 0, 3, 5]
    assert gravity_sort(input_arr) == expected
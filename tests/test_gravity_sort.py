import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_normal_case():
    """Test gravity sort with a standard list of integers"""
    input_arr = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_arr) == expected

def test_gravity_sort_already_sorted():
    """Test gravity sort with an already sorted list"""
    input_arr = [1, 2, 3, 4, 5]
    assert gravity_sort(input_arr) == input_arr

def test_gravity_sort_reverse_sorted():
    """Test gravity sort with a reverse sorted list"""
    input_arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_arr) == expected

def test_gravity_sort_empty_list():
    """Test gravity sort with an empty list"""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test gravity sort with a single element"""
    input_arr = [42]
    assert gravity_sort(input_arr) == input_arr

def test_gravity_sort_with_duplicates():
    """Test gravity sort with duplicate elements"""
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert gravity_sort(input_arr) == expected

def test_gravity_sort_negative_numbers():
    """Test that gravity sort raises an error for negative numbers"""
    with pytest.raises(ValueError, match="Gravity sort only works with non-negative integers"):
        gravity_sort([-1, 2, 3])
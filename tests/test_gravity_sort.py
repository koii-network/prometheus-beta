import pytest
import sys
import os

# Ensure src directory is in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gravity_sort import gravity_sort

def test_gravity_sort_normal_case():
    """Test gravity sort with a standard list of integers"""
    input_list = [5, 2, 9, 1, 7, 6]
    assert gravity_sort(input_list) == sorted(input_list)

def test_gravity_sort_empty_list():
    """Test gravity sort with an empty list"""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test gravity sort with a single element"""
    assert gravity_sort([42]) == [42]

def test_gravity_sort_already_sorted():
    """Test gravity sort with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == input_list

def test_gravity_sort_reverse_sorted():
    """Test gravity sort with a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert gravity_sort(input_list) == sorted(input_list)

def test_gravity_sort_with_duplicates():
    """Test gravity sort with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert gravity_sort(input_list) == sorted(input_list)

def test_gravity_sort_invalid_input_type():
    """Test gravity sort with invalid input type"""
    with pytest.raises(TypeError):
        gravity_sort("not a list")

def test_gravity_sort_negative_numbers():
    """Test gravity sort with negative numbers"""
    with pytest.raises(ValueError):
        gravity_sort([1, 2, -3, 4])
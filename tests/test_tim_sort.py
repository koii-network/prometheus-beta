import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tim_sort import tim_sort

def test_tim_sort_basic_list():
    """Test sorting a basic list of integers"""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_tim_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert tim_sort(input_list) == input_list

def test_tim_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_with_strings():
    """Test sorting a list of strings"""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_large_list():
    """Test sorting a larger list"""
    input_list = list(range(1000, 0, -1))
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        tim_sort("not a list")

def test_tim_sort_list_with_different_types():
    """Test sorting a list with mixed comparable types"""
    input_list = [3, 1.5, 'a', 2]
    expected = sorted(input_list)
    assert tim_sort(input_list) == expected

def test_tim_sort_original_list_unchanged():
    """Test that the original list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original = input_list.copy()
    tim_sort(input_list)
    assert input_list == original
import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_standard_list():
    """Test sorting a standard list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_empty_list():
    """Test sorting an empty list"""
    assert pancake_sort([]) == []

def test_pancake_sort_single_element():
    """Test sorting a list with a single element"""
    assert pancake_sort([5]) == [5]

def test_pancake_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert pancake_sort(input_list) == input_list

def test_pancake_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 4, 1, 3, 2]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-4, 2, -1, 0, 3, -5]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        pancake_sort("not a list")

def test_pancake_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected
import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_normal_list():
    """Test pancake sort with a normal unsorted list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_already_sorted():
    """Test pancake sort with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_reverse_sorted():
    """Test pancake sort with a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_single_element():
    """Test pancake sort with a single element list"""
    input_list = [42]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_empty_list():
    """Test pancake sort with an empty list"""
    input_list = []
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_with_duplicates():
    """Test pancake sort with a list containing duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_with_floats():
    """Test pancake sort with a list of floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_invalid_input():
    """Test pancake sort with an invalid input type"""
    with pytest.raises(TypeError):
        pancake_sort("not a list")
    with pytest.raises(TypeError):
        pancake_sort(123)
import pytest
from src.comb_sort import comb_sort

def test_comb_sort_standard_list():
    """Test sorting a standard list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert comb_sort(input_list) == input_list

def test_comb_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_empty_list():
    """Test sorting an empty list"""
    assert comb_sort([]) == []

def test_comb_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert comb_sort(input_list) == input_list

def test_comb_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        comb_sort("not a list")

def test_comb_sort_uncomparable_elements():
    """Test that a ValueError is raised for uncomparable elements"""
    with pytest.raises(ValueError):
        comb_sort([1, 2, "3", 4])
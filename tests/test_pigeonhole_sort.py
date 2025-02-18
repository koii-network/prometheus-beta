import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_pigeonhole_sort_normal_case():
    """Test sorting a list of integers"""
    input_list = [8, 3, 2, 7, 4, 6, 8]
    expected = [2, 3, 4, 6, 7, 8, 8]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_already_sorted():
    """Test a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == input_list

def test_pigeonhole_sort_reverse_sorted():
    """Test a list sorted in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_empty_list():
    """Test an empty list"""
    assert pigeonhole_sort([]) == []

def test_pigeonhole_sort_single_element():
    """Test a list with a single element"""
    input_list = [42]
    assert pigeonhole_sort(input_list) == input_list

def test_pigeonhole_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 7, 0, -1, 4]
    expected = [-5, -2, -1, 0, 3, 4, 7]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")

def test_pigeonhole_sort_invalid_element_type():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1, 2, "3", 4])
import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test ascending order sorting"""
    input_list = [3, 7, 4, 8, 6, 2, 1, 5]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_descending():
    """Test descending order sorting"""
    input_list = [3, 7, 4, 8, 6, 2, 1, 5]
    expected = sorted(input_list, reverse=True)
    assert bitonic_sort(input_list, ascending=False) == expected

def test_bitonic_sort_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test sorting a single element list"""
    input_list = [42]
    assert bitonic_sort(input_list) == input_list

def test_bitonic_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bitonic_sort(input_list) == input_list

def test_bitonic_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_float_numbers():
    """Test sorting floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_negative_numbers():
    """Test sorting list with negative numbers"""
    input_list = [-3, 7, -4, 8, -6, 2, -1, 5]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_input_type_error():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_mixed_type_error():
    """Test error handling for mixed type list"""
    with pytest.raises(ValueError):
        bitonic_sort([1, 2, "3", 4.0])
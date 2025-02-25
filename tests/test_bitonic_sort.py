import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test ascending order sorting"""
    input_list = [3, 7, 1, 5, 2, 8, 4, 6]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_descending():
    """Test descending order sorting"""
    input_list = [3, 7, 1, 5, 2, 8, 4, 6]
    expected = sorted(input_list, reverse=True)
    assert bitonic_sort(input_list, ascending=False) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert bitonic_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bitonic_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-3, 7, -1, 5, -2, 8, 4, -6]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")
        bitonic_sort(123)
        bitonic_sort(None)
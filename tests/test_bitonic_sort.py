import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test sorting a single-element list"""
    assert bitonic_sort([5]) == [5]

def test_bitonic_sort_ascending():
    """Test ascending sort of a random list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert bitonic_sort(input_list) == sorted(input_list)

def test_bitonic_sort_descending():
    """Test descending sort of a random list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert bitonic_sort(input_list, ascending=False) == sorted(input_list, reverse=True)

def test_bitonic_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bitonic_sort(input_list) == input_list

def test_bitonic_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert bitonic_sort(input_list) == sorted(input_list)

def test_bitonic_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert bitonic_sort(input_list) == sorted(input_list)

def test_bitonic_sort_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_preserves_original():
    """Test that the original list is not modified"""
    original = [5, 2, 9, 1, 7]
    bitonic_sort(original)
    assert original == [5, 2, 9, 1, 7]
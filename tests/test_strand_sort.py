import pytest
from src.strand_sort import strand_sort

def test_strand_sort_basic():
    """Test basic sorting functionality"""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_empty_list():
    """Test sorting an empty list"""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element"""
    assert strand_sort([42]) == [42]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -9, 1, 7, -6]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        strand_sort("not a list")
    with pytest.raises(TypeError):
        strand_sort(123)
    with pytest.raises(TypeError):
        strand_sort(None)
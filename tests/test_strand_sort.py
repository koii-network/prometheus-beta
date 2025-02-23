import pytest
from src.strand_sort import strand_sort, merge

def test_strand_sort_basic():
    """Test basic sorting functionality"""
    input_list = [4, 2, 7, 1, 5, 3]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_already_sorted():
    """Test when input is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_empty_list():
    """Test sorting an empty list"""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert strand_sort(input_list) == input_list

def test_strand_sort_large_list():
    """Test sorting a larger list"""
    import random
    input_list = [random.randint(1, 1000) for _ in range(100)]
    expected = sorted(input_list)
    assert strand_sort(input_list) == expected

def test_strand_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        strand_sort("not a list")
    with pytest.raises(TypeError):
        strand_sort(123)

def test_merge_basic():
    """Test merge functionality with two sorted lists"""
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge(list1, list2) == expected

def test_merge_empty_lists():
    """Test merge with empty lists"""
    assert merge([], []) == []
    assert merge([1, 2], []) == [1, 2]
    assert merge([], [3, 4]) == [3, 4]
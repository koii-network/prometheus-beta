import pytest
from src.list_union import find_list_union

def test_list_union_basic():
    """Test basic union of two lists"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_with_duplicates():
    """Test union with duplicate elements"""
    list1 = [1, 2, 2, 3]
    list2 = [3, 4, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_empty_lists():
    """Test union with empty lists"""
    list1 = []
    list2 = []
    assert find_list_union(list1, list2) == []

def test_list_union_one_empty_list():
    """Test union when one list is empty"""
    list1 = [1, 2, 3]
    list2 = []
    assert find_list_union(list1, list2) == [1, 2, 3]

def test_list_union_different_types():
    """Test union with lists of mixed types"""
    list1 = [1, 'a', 2]
    list2 = ['a', 3, 4]
    assert find_list_union(list1, list2) == [1, 'a', 2, 3, 4]

def test_list_union_order_preservation():
    """Test that the order of first occurrence is preserved"""
    list1 = [3, 1, 2]
    list2 = [4, 1, 5]
    assert find_list_union(list1, list2) == [3, 1, 2, 4, 5]
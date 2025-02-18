import pytest
from src.list_union import find_list_union

def test_list_union_basic():
    """Test basic union of two lists with some overlap"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_empty_lists():
    """Test union with empty lists"""
    assert find_list_union([], []) == []
    assert find_list_union([1, 2], []) == [1, 2]
    assert find_list_union([], [3, 4]) == [3, 4]

def test_list_union_duplicates():
    """Test union with lists containing duplicates"""
    list1 = [1, 2, 2, 3]
    list2 = [3, 4, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_different_types():
    """Test union with lists of different types"""
    list1 = [1, 'a', 2]
    list2 = ['a', 3, 4]
    assert find_list_union(list1, list2) == [1, 'a', 2, 3, 4]

def test_list_union_order_preservation():
    """Ensure the order of first occurrence is preserved"""
    list1 = [3, 1, 2]
    list2 = [4, 1, 5]
    assert find_list_union(list1, list2) == [3, 1, 2, 4, 5]
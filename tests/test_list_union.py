import pytest
from src.list_union import list_union

def test_list_union_basic():
    """Test basic list union functionality"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    assert list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_with_duplicates():
    """Test list union with duplicate elements"""
    list1 = [1, 2, 2, 3]
    list2 = [3, 4, 4, 5]
    assert list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_empty_lists():
    """Test list union with empty lists"""
    list1 = []
    list2 = []
    assert list_union(list1, list2) == []

def test_list_union_one_empty_list():
    """Test list union with one empty list"""
    list1 = [1, 2, 3]
    list2 = []
    assert list_union(list1, list2) == [1, 2, 3]

def test_list_union_different_types():
    """Test list union with different types of elements"""
    list1 = [1, 'a', 2]
    list2 = ['a', 3, 4]
    assert list_union(list1, list2) == [1, 'a', 2, 3, 4]

def test_list_union_order_preservation():
    """Test that the order of first occurrence is preserved"""
    list1 = [3, 1, 2]
    list2 = [4, 1, 5]
    assert list_union(list1, list2) == [3, 1, 2, 4, 5]
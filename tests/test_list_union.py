import pytest
from src.list_union import find_list_union

def test_list_union_basic():
    """Test basic union of two lists"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_with_duplicates():
    """Test union of lists with duplicates"""
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
    """Test union with different types of elements"""
    list1 = [1, 'a', 2.5]
    list2 = ['a', 3, 4.5]
    assert find_list_union(list1, list2) == [1, 'a', 2.5, 3, 4.5]
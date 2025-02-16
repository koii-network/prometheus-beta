import pytest
from src.list_union import find_list_union

def test_find_list_union_basic():
    """Test basic list union functionality"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert find_list_union(list1, list2) == expected

def test_find_list_union_duplicates():
    """Test list union with duplicates"""
    list1 = [1, 2, 2, 3]
    list2 = [3, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert find_list_union(list1, list2) == expected

def test_find_list_union_empty_lists():
    """Test list union with empty lists"""
    list1 = []
    list2 = []
    expected = []
    assert find_list_union(list1, list2) == expected

def test_find_list_union_one_empty_list():
    """Test list union with one empty list"""
    list1 = [1, 2, 3]
    list2 = []
    expected = [1, 2, 3]
    assert find_list_union(list1, list2) == expected

def test_find_list_union_different_types():
    """Test list union with different types of elements"""
    list1 = [1, 'a', 2]
    list2 = ['a', 3, 4]
    expected = [1, 'a', 2, 3, 4]
    assert find_list_union(list1, list2) == expected
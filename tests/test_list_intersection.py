import pytest
from src.list_intersection import find_list_intersection

def test_find_list_intersection_basic():
    """Test basic list intersection"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert set(find_list_intersection(list1, list2)) == {4, 5}

def test_find_list_intersection_no_match():
    """Test lists with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_list_intersection(list1, list2) == []

def test_find_list_intersection_empty_lists():
    """Test intersection with empty lists"""
    list1 = []
    list2 = [1, 2, 3]
    assert find_list_intersection(list1, list2) == []

def test_find_list_intersection_duplicates():
    """Test lists with duplicate elements"""
    list1 = [1, 2, 2, 3, 4]
    list2 = [2, 2, 4, 5, 6]
    assert set(find_list_intersection(list1, list2)) == {2, 4}

def test_find_list_intersection_different_types():
    """Test lists with different types"""
    list1 = [1, 'a', 2, 'b']
    list2 = ['a', 3, 'b', 4]
    assert set(find_list_intersection(list1, list2)) == {'a', 'b'}
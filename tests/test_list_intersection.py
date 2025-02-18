import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test basic list intersection"""
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    assert sorted(find_list_intersection(list1, list2)) == [3, 4]

def test_no_intersection():
    """Test when lists have no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_list_intersection(list1, list2) == []

def test_one_empty_list():
    """Test when one list is empty"""
    list1 = [1, 2, 3]
    list2 = []
    assert find_list_intersection(list1, list2) == []

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    list1 = [1, 2, 2, 3, 3, 4]
    list2 = [2, 3, 3, 4, 5]
    assert sorted(find_list_intersection(list1, list2)) == [2, 3, 4]

def test_different_types():
    """Test lists with different types of elements"""
    list1 = [1, 'a', 2, 3]
    list2 = ['a', 2, 4, 5]
    assert sorted(find_list_intersection(list1, list2)) == [2, 'a']
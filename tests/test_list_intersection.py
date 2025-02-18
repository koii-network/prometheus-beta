import pytest
from src.list_intersection import find_list_intersection

def test_find_list_intersection_basic():
    """Test basic intersection of two lists"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert sorted(find_list_intersection(list1, list2)) == [4, 5]

def test_find_list_intersection_no_common():
    """Test lists with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_list_intersection(list1, list2) == []

def test_find_list_intersection_duplicates():
    """Test lists with duplicate elements"""
    list1 = [1, 2, 2, 3, 3, 4]
    list2 = [2, 2, 3, 4, 4, 5]
    assert sorted(find_list_intersection(list1, list2)) == [2, 3, 4]

def test_find_list_intersection_empty_lists():
    """Test intersection with empty lists"""
    assert find_list_intersection([], [1, 2, 3]) == []
    assert find_list_intersection([1, 2, 3], []) == []
    assert find_list_intersection([], []) == []

def test_find_list_intersection_mixed_types():
    """Test intersection with mixed type elements"""
    list1 = [1, 'a', 2, 'b']
    list2 = ['a', 3, 'b', 4]
    assert sorted(find_list_intersection(list1, list2)) == ['a', 'b']
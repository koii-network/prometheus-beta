import pytest
from src.list_intersection import find_intersection

def test_basic_intersection():
    """Test intersection of lists with common elements"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert sorted(find_intersection(list1, list2)) == [4, 5]

def test_no_intersection():
    """Test lists with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_intersection(list1, list2) == []

def test_empty_lists():
    """Test intersection with empty lists"""
    list1 = []
    list2 = [1, 2, 3]
    assert find_intersection(list1, list2) == []

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    list1 = [1, 2, 2, 3, 3, 4]
    list2 = [2, 2, 4, 5, 6]
    assert sorted(find_intersection(list1, list2)) == [2, 4]

def test_identical_lists():
    """Test lists that are identical"""
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    assert sorted(find_intersection(list1, list2)) == [1, 2, 3]

def test_mixed_type_lists():
    """Test lists with mixed types"""
    list1 = [1, 'a', 2, 'b']
    list2 = ['a', 2, 'c', 3]
    assert sorted(find_intersection(list1, list2)) == [2, 'a']
import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test basic functionality of finding common elements"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert set(find_common(list1, list2)) == {4, 5}

def test_find_common_empty_lists():
    """Test with empty lists"""
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test lists with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_common(list1, list2) == []

def test_find_common_duplicate_elements():
    """Test lists with duplicate elements"""
    list1 = [1, 2, 2, 3, 3, 4]
    list2 = [2, 3, 3, 4, 5]
    assert set(find_common(list1, list2)) == {2, 3, 4}

def test_find_common_different_types():
    """Test lists with mixed types"""
    list1 = [1, 'a', 2, 'b']
    list2 = ['a', 2, 'c', 3]
    assert set(find_common(list1, list2)) == {2, 'a'}

def test_find_common_large_lists():
    """Test with larger lists"""
    list1 = list(range(1000)) + ['unique1']
    list2 = list(range(1000)) + ['unique2']
    assert set(find_common(list1, list2)) == set(range(1000))
import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test basic list intersection"""
    assert find_list_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_empty_list():
    """Test intersection with an empty list"""
    assert find_list_intersection([1, 2, 3], []) == []
    assert find_list_intersection([], [1, 2, 3]) == []

def test_no_intersection():
    """Test lists with no common elements"""
    assert find_list_intersection([1, 2, 3], [4, 5, 6]) == []

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    assert find_list_intersection([1, 2, 2, 3, 3], [2, 3, 3, 4]) == [2, 3]

def test_different_types():
    """Test intersection with different types of elements"""
    assert find_list_intersection([1, 'a', 2], ['a', 2, 3]) == ['a', 2]

def test_order_preservation():
    """Test that the order of first occurrence is preserved"""
    assert find_list_intersection([1, 2, 3, 4, 2], [2, 3, 5, 1]) == [1, 2, 3]
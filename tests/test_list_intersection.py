import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test basic list intersection"""
    assert find_list_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_string_intersection():
    """Test intersection with string lists"""
    assert find_list_intersection(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

def test_empty_list():
    """Test intersection with an empty list"""
    assert find_list_intersection([], [1, 2, 3]) == []
    assert find_list_intersection([1, 2, 3], []) == []

def test_no_intersection():
    """Test lists with no common elements"""
    assert find_list_intersection([1, 2, 3], [4, 5, 6]) == []

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    assert find_list_intersection([1, 1, 2, 2, 3], [2, 2, 3, 4, 4]) == [2, 3]

def test_type_preservation():
    """Test that the order and type of first occurrence is preserved"""
    result = find_list_intersection([1, 'a', 2, 'b'], ['a', 2, 'c', 1])
    assert result == ['a', 2, 1]
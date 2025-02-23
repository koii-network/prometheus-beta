import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test basic list intersection"""
    assert find_list_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_empty_lists():
    """Test intersection with empty lists"""
    assert find_list_intersection([], [1, 2, 3]) == []
    assert find_list_intersection([1, 2, 3], []) == []
    assert find_list_intersection([], []) == []

def test_no_intersection():
    """Test lists with no common elements"""
    assert find_list_intersection([1, 2, 3], [4, 5, 6]) == []

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    assert find_list_intersection([1, 2, 2, 3, 3], [2, 3, 3, 4]) == [2, 3]

def test_mixed_type_lists():
    """Test lists with mixed types"""
    assert find_list_intersection([1, 'a', 2, 'b'], [2, 'a', 3, 'c']) == ['a', 2]

def test_preserve_first_occurrence_order():
    """Test that order of first occurrence in list1 is preserved"""
    assert find_list_intersection([1, 2, 3, 2, 1], [2, 1, 4, 5]) == [1, 2]
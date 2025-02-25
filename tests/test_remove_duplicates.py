import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test handling of empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types and duplicates"""
    assert remove_duplicates([1, 'a', 2, 'a', 3, 1]) == [1, 'a', 2, 3]

def test_remove_duplicates_preserve_order():
    """Test that first occurrence of each element is preserved"""
    assert remove_duplicates(['b', 'a', 'c', 'a', 'b', 'd']) == ['b', 'a', 'c', 'd']
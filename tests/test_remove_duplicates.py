import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test handling of empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test list with all identical elements"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_order_preservation():
    """Test that first occurrence of each element is preserved"""
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 1, 4, 5, 9, 2, 6]

def test_remove_duplicates_mixed_types():
    """Ensure function works with different integer values"""
    assert remove_duplicates([10, -5, 0, 10, -5, 7]) == [10, -5, 0, 7]
import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types"""
    assert remove_duplicates([1, 'a', 2, 'a', 3, 1]) == [1, 'a', 2, 3]

def test_remove_duplicates_maintains_order():
    """Test that first occurrence order is maintained"""
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert remove_duplicates(test_list) == [3, 1, 4, 5, 9, 2, 6]

def test_remove_duplicates_large_input():
    """Test with a larger input to verify performance"""
    large_list = list(range(1000)) + list(range(1000))
    result = remove_duplicates(large_list)
    assert len(result) == 1000
    assert result == list(range(1000))
import pytest
from src.array_utils import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test with mixed data types"""
    assert remove_duplicates([1, 'a', 2, 'a', 1, 3]) == [1, 'a', 2, 3]

def test_remove_duplicates_invalid_input():
    """Test with invalid input type"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")

def test_remove_duplicates_order_preservation():
    """Test that the order of first occurrence is preserved"""
    assert remove_duplicates([3, 1, 2, 1, 3, 4]) == [3, 1, 2, 4]
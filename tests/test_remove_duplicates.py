import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    arr = [1, 2, 3, 2, 4, 1, 5]
    assert remove_duplicates(arr) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test empty list handling"""
    arr = []
    assert remove_duplicates(arr) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    arr = [1, 2, 3, 4, 5]
    assert remove_duplicates(arr) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    arr = [1, 1, 1, 1, 1]
    assert remove_duplicates(arr) == [1]

def test_remove_duplicates_invalid_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")

def test_remove_duplicates_invalid_elements():
    """Test handling of non-integer elements"""
    with pytest.raises(ValueError):
        remove_duplicates([1, 2, "3", 4])

def test_remove_duplicates_preserve_order():
    """Test that first occurrence order is preserved"""
    arr = [5, 2, 3, 2, 5, 1, 3]
    assert remove_duplicates(arr) == [5, 2, 3, 1]
import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

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
    """Test with a list of mixed types"""
    assert remove_duplicates([1, '1', 1, '1', 2]) == [1, '1', 2]

def test_remove_duplicates_preserves_order():
    """Test that the order of first occurrence is preserved"""
    assert remove_duplicates(['b', 'a', 'c', 'a', 'b']) == ['b', 'a', 'c']

def test_remove_duplicates_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)
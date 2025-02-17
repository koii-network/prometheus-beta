import pytest
from src.remove_duplicates import remove_duplicates

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
    """Test with a list of all duplicate values"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test with mixed type elements"""
    assert remove_duplicates([1, '1', 2, '2', 1, 2]) == [1, '1', 2, '2']

def test_remove_duplicates_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    with pytest.raises(TypeError):
        remove_duplicates(123)
    with pytest.raises(TypeError):
        remove_duplicates(None)
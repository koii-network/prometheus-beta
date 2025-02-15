import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_strings():
    """Test duplicate removal with string values"""
    assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

def test_remove_duplicates_mixed_types():
    """Test duplicate removal with mixed types"""
    assert remove_duplicates([1, '1', 1, 'a', 'a', 2]) == [1, '1', 'a', 2]

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate elements"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)
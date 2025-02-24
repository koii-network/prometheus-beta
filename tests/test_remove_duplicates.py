import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test removing duplicates from a simple list"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test removing duplicates from an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate values"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types"""
    input_list = [1, 'a', 2, 'a', 3, 1, 'b']
    expected = [1, 'a', 2, 3, 'b']
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)
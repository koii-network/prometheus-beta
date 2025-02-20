import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 2, 3, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types"""
    input_list = [1, '1', 1, 'a', 'a', 2]
    expected = [1, '1', 'a', 2]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_preserve_order():
    """Test that original order is preserved"""
    input_list = [3, 1, 2, 1, 3, 4, 2]
    expected = [3, 1, 2, 4]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)
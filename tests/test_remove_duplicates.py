import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    result = remove_duplicates(input_list)
    assert result == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test removing duplicates from an empty list"""
    input_list = []
    result = remove_duplicates(input_list)
    assert result == []

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    result = remove_duplicates(input_list)
    assert result == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate elements"""
    input_list = [1, 1, 1, 1]
    result = remove_duplicates(input_list)
    assert result == [1]

def test_remove_duplicates_mixed_types():
    """Test removing duplicates from a list with mixed types"""
    input_list = [1, 'a', 2, 'a', 3, 1]
    result = remove_duplicates(input_list)
    assert result == [1, 'a', 2, 3]

def test_remove_duplicates_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
        remove_duplicates(123)
        remove_duplicates(None)
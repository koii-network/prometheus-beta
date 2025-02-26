import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert deleteDuplicates(input_arr) == expected

def test_delete_duplicates_empty_list():
    """Test handling of empty list"""
    assert deleteDuplicates([]) == []

def test_delete_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_arr = [1, 2, 3, 4, 5]
    assert deleteDuplicates(input_arr) == input_arr

def test_delete_duplicates_all_duplicates():
    """Test list with all duplicate elements"""
    input_arr = [1, 1, 1, 1, 1]
    assert deleteDuplicates(input_arr) == [1]

def test_delete_duplicates_mixed_types():
    """Test list with mixed numeric types"""
    input_arr = [1, 1.0, 2, 2.0, 3]
    expected = [1, 2, 3]
    assert deleteDuplicates(input_arr) == expected

def test_delete_duplicates_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        deleteDuplicates("not a list")
        deleteDuplicates(123)
        deleteDuplicates(None)
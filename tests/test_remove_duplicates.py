import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates from a sorted list"""
    input_list = [1, 1, 2, 3, 3, 4, 5, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_empty_list():
    """Test an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    """Test a list with a single element"""
    input_list = [42]
    assert remove_duplicates(input_list) == [42]

def test_remove_duplicates_all_duplicates():
    """Test a list with all elements being the same"""
    input_list = [7, 7, 7, 7]
    assert remove_duplicates(input_list) == [7]

def test_remove_duplicates_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_unsorted_list():
    """Test raising ValueError for unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted"):
        remove_duplicates([3, 1, 2, 4])
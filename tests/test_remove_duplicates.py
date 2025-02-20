import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_large_list():
    """Test with a larger list with multiple duplicates"""
    input_list = [10, 20, 30, 40, 50, 20, 30, 10, 60, 70, 40, 80, 90, 50]
    expected = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate elements"""
    input_list = [5, 5, 5, 5, 5]
    assert remove_duplicates(input_list) == [5]

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_non_integer_elements():
    """Test error handling for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, 'a', 3])
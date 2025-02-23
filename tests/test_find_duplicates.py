import pytest
from src.find_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test basic duplicate finding"""
    assert sorted(find_duplicates([1, 2, 3, 4, 2, 3, 5])) == [2, 3]

def test_find_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_all_duplicates():
    """Test list with all elements duplicated"""
    assert sorted(find_duplicates([1, 1, 1, 1])) == [1]

def test_find_duplicates_empty_list():
    """Test empty list"""
    assert find_duplicates([]) == []

def test_find_duplicates_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_duplicates("not a list")

def test_find_duplicates_invalid_element_type():
    """Test list with non-integer elements raises TypeError"""
    with pytest.raises(TypeError, match="List must contain only integers"):
        find_duplicates([1, 2, '3', 4])

def test_find_duplicates_multiple_duplicates():
    """Test finding multiple duplicates with different frequencies"""
    assert sorted(find_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) == [2, 3, 4]
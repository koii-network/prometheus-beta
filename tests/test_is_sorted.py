import pytest
from src.is_sorted import is_list_sorted

def test_is_list_sorted_ascending_true():
    """Test sorted ascending list"""
    assert is_list_sorted([1, 2, 3, 4, 5]) == True

def test_is_list_sorted_ascending_false():
    """Test unsorted ascending list"""
    assert is_list_sorted([1, 3, 2, 4, 5]) == False

def test_is_list_sorted_descending_true():
    """Test sorted descending list"""
    assert is_list_sorted([5, 4, 3, 2, 1], ascending=False) == True

def test_is_list_sorted_descending_false():
    """Test unsorted descending list"""
    assert is_list_sorted([5, 3, 4, 2, 1], ascending=False) == False

def test_is_list_sorted_empty_list():
    """Test empty list"""
    assert is_list_sorted([]) == True

def test_is_list_sorted_single_element():
    """Test single element list"""
    assert is_list_sorted([42]) == True

def test_is_list_sorted_with_duplicates_ascending():
    """Test ascending list with duplicate elements"""
    assert is_list_sorted([1, 2, 2, 3, 4]) == True

def test_is_list_sorted_with_duplicates_descending():
    """Test descending list with duplicate elements"""
    assert is_list_sorted([5, 4, 4, 3, 2], ascending=False) == True

def test_is_list_sorted_invalid_input():
    """Test invalid input raises TypeError"""
    with pytest.raises(TypeError):
        is_list_sorted("not a list")

def test_is_list_sorted_numeric_mixed():
    """Test sorting of mixed numeric types"""
    assert is_list_sorted([1, 2.5, 3, 4, 5]) == True
    assert is_list_sorted([5, 4.5, 3, 2, 1], ascending=False) == True
import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert deleteDuplicates(arr) == expected

def test_delete_duplicates_empty_list():
    """Test with an empty list"""
    arr = []
    expected = []
    assert deleteDuplicates(arr) == expected

def test_delete_duplicates_no_duplicates():
    """Test with a list that has no duplicates"""
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert deleteDuplicates(arr) == expected

def test_delete_duplicates_all_duplicates():
    """Test with a list of all duplicate elements"""
    arr = [1, 1, 1, 1, 1]
    expected = [1]
    assert deleteDuplicates(arr) == expected

def test_delete_duplicates_multiple_types_of_duplicates():
    """Test with multiple types of duplicates in different positions"""
    arr = [5, 2, 5, 3, 2, 1, 5, 3]
    expected = [5, 2, 3, 1]
    assert deleteDuplicates(arr) == expected
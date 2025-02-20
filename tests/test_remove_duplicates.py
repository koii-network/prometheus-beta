import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_arr) == expected

def test_remove_duplicates_empty():
    """Test with an empty array"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with an array that has no duplicates"""
    input_arr = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_arr) == input_arr

def test_remove_duplicates_all_duplicates():
    """Test with an array of all duplicate elements"""
    input_arr = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_arr) == [1]

def test_remove_duplicates_mixed_types():
    """Test with mixed numeric types"""
    input_arr = [1, 2, 2.0, 3, 3.0, 4]
    expected = [1, 2, 3, 4]
    assert remove_duplicates(input_arr) == expected
import pytest
from src.array_utils import deleteDuplicates

def test_deleteDuplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert deleteDuplicates(input_arr) == expected

def test_deleteDuplicates_no_duplicates():
    """Test array with no duplicates"""
    input_arr = [1, 2, 3, 4, 5]
    assert deleteDuplicates(input_arr) == input_arr

def test_deleteDuplicates_all_duplicates():
    """Test array with all duplicate elements"""
    input_arr = [1, 1, 1, 1, 1]
    assert deleteDuplicates(input_arr) == [1]

def test_deleteDuplicates_empty_array():
    """Test empty array"""
    input_arr = []
    assert deleteDuplicates(input_arr) == []

def test_deleteDuplicates_preserve_order():
    """Test that original order of first occurrence is preserved"""
    input_arr = [5, 2, 6, 2, 5, 1, 6, 3]
    expected = [5, 2, 6, 1, 3]
    assert deleteDuplicates(input_arr) == expected
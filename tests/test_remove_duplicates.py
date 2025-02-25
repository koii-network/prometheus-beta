import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test handling of an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate elements"""
    input_list = [1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types"""
    input_list = [1, 'a', 2, 'a', 3, 1]
    expected = [1, 'a', 2, 3]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_order_preservation():
    """Test that the first occurrence of each element is preserved"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [3, 1, 4, 5, 9, 2, 6]
    assert remove_duplicates(input_list) == expected
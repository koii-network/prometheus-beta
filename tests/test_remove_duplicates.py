import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_list = [1, 2, 3, 2, 1, 4, 5, 4]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test removing duplicates from an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test removing duplicates with mixed types"""
    input_list = [1, 'a', 2, 'a', 3, 1, 4]
    expected = [1, 'a', 2, 3, 4]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_preserves_order():
    """Test that the order of first occurrence is preserved"""
    input_list = [5, 2, 3, 2, 5, 1, 4, 1]
    expected = [5, 2, 3, 1, 4]
    assert remove_duplicates(input_list) == expected
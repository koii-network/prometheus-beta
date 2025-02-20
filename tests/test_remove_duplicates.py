import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicates"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_order_preservation():
    """Test that the original order is preserved"""
    input_list = [5, 2, 3, 2, 5, 1, 3]
    expected = [5, 2, 3, 1]
    assert remove_duplicates(input_list) == expected
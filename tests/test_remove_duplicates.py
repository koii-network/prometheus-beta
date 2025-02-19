import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test removing duplicates from a simple list"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate elements"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test with mixed types of elements"""
    input_list = [1, 'a', 2, 'a', 3, 1, 'b']
    expected = [1, 'a', 2, 3, 'b']
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_preserves_order():
    """Ensure the original order is preserved"""
    input_list = [3, 1, 2, 1, 3, 4, 2, 5]
    expected = [3, 1, 2, 4, 5]
    assert remove_duplicates(input_list) == expected
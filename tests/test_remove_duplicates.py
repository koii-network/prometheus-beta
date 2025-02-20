import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_changes():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1, 1]
    expected = [1]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_complex_scenario():
    """Test a more complex scenario with multiple duplicates"""
    input_list = [10, 5, 2, 10, 3, 7, 5, 8, 2, 9, 7, 1]
    expected = [10, 5, 2, 3, 7, 8, 9, 1]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_preserves_first_occurrence():
    """Ensure first occurrence is preserved"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [3, 1, 4, 5, 9, 2, 6]
    assert remove_duplicates(input_list) == expected
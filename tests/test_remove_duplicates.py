import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test removing duplicates from a sorted list"""
    input_list = [1, 1, 2, 3, 3, 4, 5, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_already_unique():
    """Test a list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_empty_list():
    """Test an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    """Test a list with a single element"""
    input_list = [42]
    assert remove_duplicates(input_list) == [42]

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate elements"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_negative_numbers():
    """Test with negative and positive numbers"""
    input_list = [-3, -3, -2, -1, 0, 0, 1, 2, 2, 3]
    expected = [-3, -2, -1, 0, 1, 2, 3]
    assert remove_duplicates(input_list) == expected
import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates from a sorted list"""
    input_list = [1, 1, 2, 3, 3, 4, 5, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test function with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    """Test function with a single element list"""
    assert remove_duplicates([42]) == [42]

def test_remove_duplicates_no_duplicates():
    """Test function with a list that has no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test function with a list of all duplicate elements"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_negative_numbers():
    """Test function with negative numbers and duplicates"""
    input_list = [-3, -3, -2, -1, -1, 0, 0, 1, 1]
    expected = [-3, -2, -1, 0, 1]
    assert remove_duplicates(input_list) == expected
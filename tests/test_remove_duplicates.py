import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_mixed_order():
    """Test mixed order duplicates"""
    input_list = [5, 2, 5, 1, 2, 3, 5, 4, 1]
    expected = [5, 2, 1, 3, 4]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_large_list():
    """Test a large list of unique and duplicate integers"""
    input_list = list(range(20)) + [5, 10, 15, 0, 19]
    expected = list(range(20))
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_negative_numbers():
    """Test list with negative numbers"""
    input_list = [-1, 2, -1, 3, 2, -5, 4]
    expected = [-1, 2, 3, -5, 4]
    assert remove_duplicates(input_list) == expected
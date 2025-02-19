import pytest
from src.filter_odd_numbers import filter_odd_numbers

def test_filter_odd_numbers_basic():
    """Test filtering odd numbers from a mixed list of integers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_odd_numbers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_empty_list():
    """Test with an empty list"""
    assert filter_odd_numbers([]) == []

def test_filter_odd_numbers_no_odds():
    """Test a list with no odd numbers"""
    assert filter_odd_numbers([2, 4, 6, 8]) == []

def test_filter_odd_numbers_all_odds():
    """Test a list with only odd numbers"""
    assert filter_odd_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_filter_odd_numbers_with_non_integers():
    """Test a list with non-integer elements"""
    input_list = [1, 2.5, 3, 'a', 4, 5, None]
    assert filter_odd_numbers(input_list) == [1, 3, 5]

def test_filter_odd_numbers_none_input():
    """Test with None input"""
    assert filter_odd_numbers(None) == []

def test_filter_odd_numbers_negative_odds():
    """Test with negative odd numbers"""
    input_list = [-1, -2, -3, -4, -5]
    assert filter_odd_numbers(input_list) == [-1, -3, -5]
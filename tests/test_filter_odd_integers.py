import pytest
from src.filter_odd_integers import filter_odd_integers

def test_filter_odd_integers_basic():
    """Test filtering and sorting odd integers from a mixed list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_integers_empty_list():
    """Test with an empty list"""
    assert filter_odd_integers([]) == []

def test_filter_odd_integers_no_odds():
    """Test with a list containing only even numbers"""
    assert filter_odd_integers([2, 4, 6, 8, 10]) == []

def test_filter_odd_integers_only_odds():
    """Test with a list containing only odd numbers"""
    input_list = [9, 3, 7, 1, 5]
    assert filter_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_integers_negative_numbers():
    """Test with negative odd and even numbers"""
    input_list = [-1, -2, -3, 0, 1, 2, 3]
    assert filter_odd_integers(input_list) == [-3, -1, 1, 3]
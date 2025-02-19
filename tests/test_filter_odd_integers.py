import pytest
from src.filter_odd_integers import filter_odd_integers

def test_filter_odd_integers_normal_case():
    """Test filtering and sorting odd integers from a mixed list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_result = [1, 3, 5, 7, 9]
    assert filter_odd_integers(input_list) == expected_result

def test_filter_odd_integers_empty_list():
    """Test with an empty list"""
    assert filter_odd_integers([]) == []

def test_filter_odd_integers_no_odds():
    """Test with a list containing only even numbers"""
    assert filter_odd_integers([2, 4, 6, 8, 10]) == []

def test_filter_odd_integers_all_odds():
    """Test with a list containing only odd numbers"""
    input_list = [11, 3, 7, 1, 9, 5]
    expected_result = [1, 3, 5, 7, 9, 11]
    assert filter_odd_integers(input_list) == expected_result

def test_filter_odd_integers_negative_numbers():
    """Test with negative numbers"""
    input_list = [-1, -2, -3, 0, 1, 2, 3]
    expected_result = [-3, -1, 1, 3]
    assert filter_odd_integers(input_list) == expected_result
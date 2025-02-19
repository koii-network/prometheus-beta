import pytest
from src.extract_odd_integers import extract_odd_integers

def test_extract_odd_integers_normal_case():
    """Test with a mix of odd and even integers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert extract_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_extract_odd_integers_all_even():
    """Test with all even integers"""
    input_list = [2, 4, 6, 8, 10]
    assert extract_odd_integers(input_list) == []

def test_extract_odd_integers_all_odd():
    """Test with all odd integers"""
    input_list = [1, 3, 5, 7, 9]
    assert extract_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_extract_odd_integers_empty_list():
    """Test with an empty list"""
    input_list = []
    assert extract_odd_integers(input_list) == []

def test_extract_odd_integers_negative_numbers():
    """Test with negative numbers"""
    input_list = [-1, -2, -3, 0, 1, 2, 3]
    assert extract_odd_integers(input_list) == [-3, -1, 1, 3]
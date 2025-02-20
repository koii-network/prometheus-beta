import pytest
from src.filter_even_numbers import filter_even_numbers

def test_filter_even_numbers_basic():
    """Test filtering even numbers from a mixed list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_all_odd():
    """Test with a list containing only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_all_even():
    """Test with a list containing only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_empty_list():
    """Test with an empty list"""
    input_list = []
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_negative():
    """Test with negative numbers"""
    input_list = [-1, -2, -3, -4, -5, -6]
    expected = [-2, -4, -6]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_zero():
    """Test handling of zero"""
    input_list = [0, 1, 2, 3, 4, 5]
    expected = [0, 2, 4]
    assert filter_even_numbers(input_list) == expected
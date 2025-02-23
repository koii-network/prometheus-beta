import pytest
from src.extract_even_numbers import extract_even_numbers

def test_extract_even_numbers_basic():
    """Test extracting even numbers from a mixed list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_empty_list():
    """Test with an empty list"""
    assert extract_even_numbers([]) == []

def test_extract_even_numbers_no_evens():
    """Test with a list containing only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert extract_even_numbers(input_list) == []

def test_extract_even_numbers_all_even():
    """Test with a list containing only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    assert extract_even_numbers(input_list) == input_list

def test_extract_even_numbers_negative_numbers():
    """Test with negative numbers"""
    input_list = [-1, -2, -3, -4, 0, 1, 2, 3, 4]
    expected = [-2, -4, 0, 2, 4]
    assert extract_even_numbers(input_list) == expected
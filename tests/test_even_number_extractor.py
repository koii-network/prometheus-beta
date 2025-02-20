import pytest
from src.even_number_extractor import extract_even_numbers

def test_extract_even_numbers_standard_case():
    """Test extraction of even numbers from a mixed list of integers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_only_odd():
    """Test case with only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert extract_even_numbers(input_list) == []

def test_extract_even_numbers_only_even():
    """Test case with only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    assert extract_even_numbers(input_list) == input_list

def test_extract_even_numbers_empty_list():
    """Test case with an empty list"""
    input_list = []
    assert extract_even_numbers(input_list) == []

def test_extract_even_numbers_negative_numbers():
    """Test case with negative numbers"""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [-4, -2, 0, 2, 4]
    assert extract_even_numbers(input_list) == expected
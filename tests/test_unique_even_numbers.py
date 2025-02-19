import pytest
from src.unique_even_numbers import get_unique_even_numbers

def test_unique_even_numbers_basic():
    """Test basic functionality with a mix of numbers"""
    input_list = [1, 2, 3, 4, 2, 6, 4, 8]
    expected = [2, 4, 6, 8]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_empty_list():
    """Test with an empty list"""
    assert get_unique_even_numbers([]) == []

def test_unique_even_numbers_no_evens():
    """Test with a list containing no even numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert get_unique_even_numbers(input_list) == []

def test_unique_even_numbers_all_even():
    """Test with a list of all even numbers"""
    input_list = [2, 4, 6, 8, 2, 4, 6]
    expected = [2, 4, 6, 8]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_large_numbers():
    """Test with large even and odd numbers"""
    input_list = [10000, -2, 3, -10000, 4, 2, -2, 10000]
    expected = [10000, -2, -10000, 4, 2]
    assert get_unique_even_numbers(input_list) == expected
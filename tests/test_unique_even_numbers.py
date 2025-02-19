import pytest
from src.unique_even_numbers import get_unique_even_numbers

def test_unique_even_numbers_basic():
    """Test basic functionality of getting unique even numbers"""
    input_list = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8]
    expected = [2, 4, 6, 8]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_empty_list():
    """Test with an empty list"""
    assert get_unique_even_numbers([]) == []

def test_unique_even_numbers_no_evens():
    """Test with a list containing no even numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert get_unique_even_numbers(input_list) == []

def test_unique_even_numbers_only_evens():
    """Test with a list containing only even numbers"""
    input_list = [2, 4, 2, 6, 4, 8]
    expected = [2, 4, 6, 8]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_negative():
    """Test with negative even numbers"""
    input_list = [-1, -2, 3, -2, 4, -4, 5, 6]
    expected = [-2, 4, -4, 6]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_order():
    """Test that the original order is preserved"""
    input_list = [8, 2, 4, 2, 6, 8, 10, 4]
    expected = [8, 2, 4, 6, 10]
    assert get_unique_even_numbers(input_list) == expected
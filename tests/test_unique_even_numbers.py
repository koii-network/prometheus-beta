import pytest
from src.unique_even_numbers import get_unique_even_numbers

def test_unique_even_numbers_basic():
    """Test basic functionality of unique even numbers"""
    input_list = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8]
    expected = [2, 4, 6, 8]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_empty_list():
    """Test with an empty list"""
    assert get_unique_even_numbers([]) == []

def test_unique_even_numbers_no_evens():
    """Test with a list containing no even numbers"""
    assert get_unique_even_numbers([1, 3, 5, 7]) == []

def test_unique_even_numbers_all_evens():
    """Test with a list of all even numbers"""
    input_list = [2, 4, 6, 2, 4, 8, 6]
    expected = [2, 4, 6, 8]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_negative_evens():
    """Test with negative even numbers"""
    input_list = [-2, 1, -4, 3, -2, 5, -4, 7]
    expected = [-2, -4]
    assert get_unique_even_numbers(input_list) == expected

def test_unique_even_numbers_order_preservation():
    """Test that original order of first appearance is preserved"""
    input_list = [8, 2, 3, 4, 2, 5, 8, 6, 4]
    expected = [8, 2, 4, 6]
    assert get_unique_even_numbers(input_list) == expected
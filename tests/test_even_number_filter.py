import pytest
from src.even_number_filter import filter_even_numbers

def test_filter_even_numbers_normal_case():
    """Test filtering even numbers from a mixed list of integers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_result = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected_result

def test_filter_even_numbers_all_odd():
    """Test filtering from a list with only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    expected_result = []
    assert filter_even_numbers(input_list) == expected_result

def test_filter_even_numbers_all_even():
    """Test filtering from a list with only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    expected_result = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected_result

def test_filter_even_numbers_empty_list():
    """Test filtering from an empty list"""
    input_list = []
    expected_result = []
    assert filter_even_numbers(input_list) == expected_result

def test_filter_even_numbers_zero_and_negatives():
    """Test filtering a list with zero and negative numbers"""
    input_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    expected_result = [-4, -2, 0, 2, 4]
    assert filter_even_numbers(input_list) == expected_result
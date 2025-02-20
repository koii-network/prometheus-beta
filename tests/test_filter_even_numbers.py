import pytest
from src.filter_even_numbers import filter_even_numbers

def test_filter_even_numbers_basic():
    """Test basic functionality of filtering even numbers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_all_odd():
    """Test a list with only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_all_even():
    """Test a list with only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_empty_list():
    """Test an empty list"""
    input_list = []
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_negative_numbers():
    """Test list with negative numbers"""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [-4, -2, 0, 2, 4]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_sorted_input():
    """Test that the function works with an already sorted input"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    result = filter_even_numbers(input_list)
    assert result == expected
    # Verify that the original order is maintained
    assert all(result[i] <= result[i+1] for i in range(len(result)-1))
import pytest
from src.even_numbers_filter import filter_even_numbers

def test_filter_even_numbers_standard():
    """Test filtering even numbers from a mixed sorted list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_empty_list():
    """Test filtering even numbers from an empty list"""
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_no_evens():
    """Test filtering when no even numbers are present"""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_only_evens():
    """Test filtering when all numbers are even"""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_negative_numbers():
    """Test filtering even numbers including negative numbers"""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [-4, -2, 0, 2, 4]
    assert filter_even_numbers(input_list) == expected
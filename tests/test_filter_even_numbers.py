import pytest
from src.filter_even_numbers import filter_even_numbers

def test_filter_even_numbers_normal_case():
    """Test filtering even numbers from a mixed list of integers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_only_odd():
    """Test case where no even numbers are present"""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_only_even():
    """Test case where all numbers are even"""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_negative_numbers():
    """Test filtering even numbers including negative integers"""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [-4, -2, 0, 2, 4]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_empty_list():
    """Test with an empty list"""
    input_list = []
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_invalid_input():
    """Test handling of invalid input"""
    with pytest.raises(TypeError):
        filter_even_numbers("not a list")
    with pytest.raises(TypeError):
        filter_even_numbers(123)
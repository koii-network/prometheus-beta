import pytest
from src.even_numbers_filter import filter_even_numbers

def test_filter_even_numbers_standard_case():
    """Test filtering even numbers from a standard sorted list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert filter_even_numbers(input_list) == [2, 4, 6, 8, 10]

def test_filter_even_numbers_only_odd():
    """Test a list with only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_only_even():
    """Test a list with only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == [2, 4, 6, 8, 10]

def test_filter_even_numbers_empty_list():
    """Test an empty list"""
    input_list = []
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_negative_numbers():
    """Test a list with negative even and odd numbers"""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert filter_even_numbers(input_list) == [-4, -2, 0, 2, 4]

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_even_numbers("not a list")

def test_unsorted_list():
    """Test raising ValueError for unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted"):
        filter_even_numbers([3, 1, 2, 4, 5])

def test_list_with_duplicates():
    """Test raising ValueError for list with duplicates"""
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        filter_even_numbers([1, 2, 2, 3, 4, 5])
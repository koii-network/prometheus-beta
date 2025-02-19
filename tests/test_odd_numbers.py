import pytest
from src.odd_numbers import extract_odd_numbers

def test_extract_odd_numbers_normal_case():
    """Test extracting odd numbers from a mixed list of integers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert extract_odd_numbers(input_list) == [1, 3, 5, 7, 9]

def test_extract_odd_numbers_only_odd():
    """Test input with only odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert extract_odd_numbers(input_list) == [1, 3, 5, 7, 9]

def test_extract_odd_numbers_only_even():
    """Test input with only even numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert extract_odd_numbers(input_list) == []

def test_extract_odd_numbers_empty_list():
    """Test extracting odd numbers from an empty list."""
    input_list = []
    assert extract_odd_numbers(input_list) == []

def test_extract_odd_numbers_negative_numbers():
    """Test extracting odd numbers including negative numbers."""
    input_list = [-1, -2, 0, 1, 2, 3]
    assert extract_odd_numbers(input_list) == [-1, 1, 3]

def test_extract_odd_numbers_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        extract_odd_numbers(123)

def test_extract_odd_numbers_non_integer_elements():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        extract_odd_numbers([1, 2, 'three', 4])
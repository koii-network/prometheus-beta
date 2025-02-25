import pytest
from src.unique_even_filter import filter_unique_even_numbers

def test_basic_even_number_filtering():
    """Test filtering unique even numbers from a mixed list."""
    input_list = [1, 2, 3, 4, 2, 5, 6, 4]
    assert filter_unique_even_numbers(input_list) == [2, 4, 6]

def test_no_even_numbers():
    """Test list with no even numbers."""
    input_list = [1, 3, 5, 7]
    assert filter_unique_even_numbers(input_list) == []

def test_empty_list():
    """Test filtering an empty list."""
    input_list = []
    assert filter_unique_even_numbers(input_list) == []

def test_only_even_numbers():
    """Test list with only even numbers."""
    input_list = [2, 4, 6, 2, 4, 8]
    assert filter_unique_even_numbers(input_list) == [2, 4, 6, 8]

def test_negative_even_numbers():
    """Test filtering lists with negative even numbers."""
    input_list = [-2, 1, -4, 3, -2, 5, -4]
    assert filter_unique_even_numbers(input_list) == [-2, -4]

def test_large_numbers():
    """Test filtering with large even numbers."""
    input_list = [1000000, 2, 1000000, 4, 2]
    assert filter_unique_even_numbers(input_list) == [1000000, 2, 4]
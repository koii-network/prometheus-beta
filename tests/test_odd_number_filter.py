import pytest
from src.odd_number_filter import filter_odd_numbers

def test_filter_odd_numbers_basic():
    """Test filtering odd numbers from a mixed array."""
    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert filter_odd_numbers(input_array) == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_only_odd():
    """Test array with only odd numbers."""
    input_array = [1, 3, 5, 7, 9]
    assert filter_odd_numbers(input_array) == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_only_even():
    """Test array with only even numbers."""
    input_array = [2, 4, 6, 8, 10]
    assert filter_odd_numbers(input_array) == []

def test_filter_odd_numbers_empty_list():
    """Test empty input array."""
    input_array = []
    assert filter_odd_numbers(input_array) == []

def test_filter_odd_numbers_negative():
    """Test array with negative numbers."""
    input_array = [-1, -2, -3, -4, -5]
    assert filter_odd_numbers(input_array) == [-1, -3, -5]

def test_filter_odd_numbers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("not a list")

def test_filter_odd_numbers_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_odd_numbers([1, 2, "3", 4, 5])
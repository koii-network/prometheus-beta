import pytest
from src.odd_numbers_filter import filter_odd_numbers

def test_filter_odd_numbers_basic():
    """Test filtering odd numbers from a mixed list of integers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [1, 3, 5, 7, 9]
    assert filter_odd_numbers(input_list) == expected

def test_filter_odd_numbers_empty_list():
    """Test filtering odd numbers from an empty list."""
    assert filter_odd_numbers([]) == []

def test_filter_odd_numbers_no_odds():
    """Test filtering from a list with no odd numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert filter_odd_numbers(input_list) == []

def test_filter_odd_numbers_only_odds():
    """Test filtering from a list with only odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert filter_odd_numbers(input_list) == input_list

def test_filter_odd_numbers_negative_odds():
    """Test filtering odd numbers including negative numbers."""
    input_list = [-1, -2, -3, 0, 1, 2, 3]
    expected = [-1, -3, 1, 3]
    assert filter_odd_numbers(input_list) == expected

def test_filter_odd_numbers_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("not a list")

def test_filter_odd_numbers_invalid_element_type():
    """Test that a TypeError is raised for non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        filter_odd_numbers([1, 2, "three", 4])

def test_filter_odd_numbers_float_handling():
    """Test handling of float numbers in the input."""
    input_list = [1.5, 2, 3.0, 4, 5.7]
    expected = []
    assert filter_odd_numbers(input_list) == expected
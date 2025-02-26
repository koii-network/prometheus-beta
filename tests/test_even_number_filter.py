import pytest
from src.even_number_filter import filter_even_numbers

def test_filter_even_numbers_basic():
    """Test filtering even numbers from a mixed list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_empty_list():
    """Test filtering an empty list."""
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_no_evens():
    """Test a list with no even numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_all_even():
    """Test a list with all even numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_negative_evens():
    """Test filtering even numbers including negative numbers."""
    input_list = [-1, -2, 0, 1, 2, 3, 4, -3, -4]
    expected = [-2, 0, 2, 4, -4]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_even_numbers("not a list")

def test_filter_even_numbers_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_even_numbers([1, 2, "3", 4])

def test_filter_even_numbers_large_list():
    """Test filtering a large list of numbers."""
    input_list = list(range(1000))
    expected = [num for num in input_list if num % 2 == 0]
    assert filter_even_numbers(input_list) == expected
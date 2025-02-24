import pytest
from src.even_number_filter import filter_even_numbers

def test_filter_even_numbers_basic():
    """Test filtering even numbers from a mixed list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_empty_list():
    """Test filtering from an empty list."""
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_no_evens():
    """Test list with no even numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_only_evens():
    """Test list with only even numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_negative_numbers():
    """Test filtering with negative even and odd numbers."""
    input_list = [-1, -2, -3, -4, 0, 1, 2, 3, 4]
    expected = [-2, -4, 0, 2, 4]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_even_numbers("not a list")

def test_filter_even_numbers_invalid_element_type():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_even_number_filter([1, 2, "3", 4])

def test_filter_even_numbers_large_list():
    """Test filtering a large list to ensure linear time complexity."""
    large_list = list(range(10000))
    result = filter_even_numbers(large_list)
    assert len(result) == 5000
    assert all(num % 2 == 0 for num in result)
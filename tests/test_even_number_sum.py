import pytest
from src.even_number_sum import sum_even_numbers

def test_sum_even_numbers_basic():
    """Test summing even numbers in a simple list."""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_numbers_empty_list():
    """Test summing even numbers in an empty list."""
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_no_evens():
    """Test list with no even numbers."""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_sum_even_numbers_all_even():
    """Test list with all even numbers."""
    assert sum_even_numbers([2, 4, 6, 8]) == 20

def test_sum_even_numbers_negative_evens():
    """Test list with negative even numbers."""
    assert sum_even_numbers([-2, -4, 1, 3]) == -6

def test_sum_even_numbers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_even_numbers("not a list")

def test_sum_even_numbers_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, '3', 4])
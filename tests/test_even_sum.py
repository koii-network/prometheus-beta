import pytest
from src.even_sum import sum_even_numbers

def test_sum_even_numbers_basic():
    """Test basic functionality with mixed even and odd numbers."""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_numbers_all_even():
    """Test with all even numbers."""
    assert sum_even_numbers([2, 4, 6, 8]) == 20

def test_sum_even_numbers_no_even():
    """Test with no even numbers."""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_sum_even_numbers_empty_list():
    """Test with an empty list."""
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_negative_even():
    """Test with negative even numbers."""
    assert sum_even_numbers([-2, -4, 1, 3, 5]) == -6

def test_sum_even_numbers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_even_numbers("not a list")

def test_sum_even_numbers_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, "3", 4])
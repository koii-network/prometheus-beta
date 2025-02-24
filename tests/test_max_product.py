import pytest
from src.max_product import max_two_number_product

def test_basic_positive_numbers():
    """Test with basic positive numbers."""
    assert max_two_number_product([1, 2, 3, 4]) == 12

def test_with_negative_numbers():
    """Test with list containing negative numbers."""
    assert max_two_number_product([-10, -3, 5, 6, -2]) == 30

def test_two_number_list():
    """Test with exactly two numbers."""
    assert max_two_number_product([5, 3]) == 15

def test_all_negative_numbers():
    """Test with all negative numbers."""
    assert max_two_number_product([-1, -2, -3, -4]) == 12

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert max_two_number_product([-10, 3, -5, 6, 2]) == 60

def test_raises_error_on_single_element():
    """Test that ValueError is raised for single-element list."""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_two_number_product([42])

def test_raises_error_on_empty_list():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_two_number_product([])

def test_raises_error_on_non_list():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_two_number_product("not a list")

def test_raises_error_on_non_integer_list():
    """Test that TypeError is raised for list with non-integer elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        max_two_number_product([1, 2, "3", 4])
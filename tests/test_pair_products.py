import pytest
from src.pair_products import calculate_pair_products

def test_basic_pair_products():
    """Test basic functionality with a simple list of integers"""
    result = calculate_pair_products([1, 2, 3])
    assert result == [2, 3, 6]

def test_empty_list():
    """Test with an empty list"""
    result = calculate_pair_products([])
    assert result == []

def test_single_element_list():
    """Test with a list containing only one element"""
    result = calculate_pair_products([5])
    assert result == []

def test_list_with_negative_numbers():
    """Test with a list containing negative numbers"""
    result = calculate_pair_products([-1, 2, -3])
    assert result == [-2, 3, -6, 2, -6, -2]

def test_invalid_input_type():
    """Test that a TypeError is raised when input is not a list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_pair_products("not a list")

def test_non_integer_list():
    """Test that a ValueError is raised when list contains non-integers"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        calculate_pair_products([1, 2, "3"])
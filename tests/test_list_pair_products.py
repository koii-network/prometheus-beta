import pytest
from src.list_pair_products import calculate_pair_products

def test_calculate_pair_products_basic():
    """Test basic functionality with a simple list of integers."""
    result = calculate_pair_products([1, 2, 3])
    assert result == [2, 3, 6]

def test_calculate_pair_products_with_negatives():
    """Test functionality with negative numbers."""
    result = calculate_pair_products([-1, 2, -3])
    assert result == [-6, -2, 3]

def test_calculate_pair_products_with_zero():
    """Test list containing zero."""
    result = calculate_pair_products([0, 1, 2])
    assert result == [0, 0, 2]

def test_calculate_pair_products_single_element():
    """Test list with only one element (should raise ValueError)."""
    with pytest.raises(ValueError):
        calculate_pair_products([5])

def test_calculate_pair_products_empty_list():
    """Test empty list raises ValueError."""
    with pytest.raises(ValueError):
        calculate_pair_products([])

def test_calculate_pair_products_invalid_input_type():
    """Test non-list input raises TypeError."""
    with pytest.raises(TypeError):
        calculate_pair_products("not a list")

def test_calculate_pair_products_non_integer_elements():
    """Test list with non-integer elements raises TypeError."""
    with pytest.raises(TypeError):
        calculate_pair_products([1, 2, "3"])

def test_calculate_pair_products_large_numbers():
    """Test with larger numbers to ensure no integer overflow."""
    result = calculate_pair_products([10, 20, 30])
    assert result == [200, 300, 600]
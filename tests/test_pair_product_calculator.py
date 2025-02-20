import pytest
from src.pair_product_calculator import calculate_pair_products

def test_normal_list():
    """Test with a normal list of integers."""
    result = calculate_pair_products([1, 2, 3])
    assert set(result) == {((1, 2), 2), ((1, 3), 3), ((2, 3), 6)}

def test_empty_list():
    """Test with an empty list."""
    assert calculate_pair_products([]) == []

def test_single_element_list():
    """Test with a list containing only one element."""
    assert calculate_pair_products([5]) == []

def test_list_with_negative_numbers():
    """Test with a list containing negative numbers."""
    result = calculate_pair_products([-1, 2, -3])
    assert set(result) == {((-1, 2), -2), ((-1, -3), 3), ((2, -3), -6)}

def test_list_with_zero():
    """Test with a list containing zero."""
    result = calculate_pair_products([0, 1, 2])
    assert set(result) == {((0, 1), 0), ((0, 2), 0), ((1, 2), 2)}

def test_large_list():
    """Test with a larger list to ensure performance."""
    numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
    result = calculate_pair_products(numbers)
    assert len(result) == 10  # Number of unique pairs
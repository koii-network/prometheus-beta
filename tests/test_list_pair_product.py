import pytest
from src.list_pair_product import calculate_pair_products

def test_normal_list():
    """Test calculation of pair products for a normal list."""
    assert sorted(calculate_pair_products([1, 2, 3])) == [2, 3, 6]

def test_empty_list():
    """Test behavior with an empty list."""
    assert calculate_pair_products([]) == []

def test_single_element_list():
    """Test behavior with a list containing a single element."""
    assert calculate_pair_products([5]) == []

def test_negative_numbers():
    """Test calculation with negative numbers."""
    assert sorted(calculate_pair_products([-1, 2, -3])) == [-6, -2, 3]

def test_zero_in_list():
    """Test calculation with zero in the list."""
    assert sorted(calculate_pair_products([0, 1, 2])) == [0, 0, 2]

def test_type_error_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_pair_products("not a list")

def test_type_error_non_integer_elements():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pair_products([1, 2, "3"])
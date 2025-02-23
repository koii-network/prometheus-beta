import pytest
from src.pair_products import calculate_pair_products

def test_normal_list():
    # Test a normal list of integers
    result = calculate_pair_products([1, 2, 3, 4])
    assert set(result) == {2, 3, 4, 6, 8, 12}
    assert len(result) == 6

def test_negative_numbers():
    # Test a list with negative numbers
    result = calculate_pair_products([-1, 2, -3, 4])
    assert set(result) == {-2, -4, 3, -12, 6, -3, 12, -8}
    assert len(result) == 6

def test_zero_included():
    # Test a list including zero
    result = calculate_pair_products([0, 2, 3])
    assert set(result) == {0, 0, 6}

def test_single_element_error():
    # Test raising ValueError for single element list
    with pytest.raises(ValueError, match="Input list must contain at least 2 elements"):
        calculate_pair_products([5])

def test_empty_list_error():
    # Test raising ValueError for empty list
    with pytest.raises(ValueError, match="Input list must contain at least 2 elements"):
        calculate_pair_products([])

def test_non_list_input():
    # Test raising TypeError for non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_pair_products("not a list")

def test_non_integer_input():
    # Test raising TypeError for non-integer elements
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pair_products([1, 2, "3", 4])
import pytest
from src.product_except_self import product_except_self

def test_basic_functionality():
    """Test basic functionality with a standard list of integers."""
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_with_zeros():
    """Test functionality when the list contains zeros."""
    assert product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]
    assert product_except_self([1, 0, 2, 3]) == [0, 6, 0, 0]

def test_negative_numbers():
    """Test functionality with negative numbers."""
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_single_element():
    """Test behavior with a single-element list."""
    assert product_except_self([5]) == [1]

def test_empty_list():
    """Test behavior with an empty list."""
    assert product_except_self([]) == []

def test_large_values():
    """Test functionality with larger values to check for potential overflow."""
    assert product_except_self([10, 20, 30, 40]) == [24000, 12000, 8000, 6000]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        product_except_self("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        product_except_self(123)

def test_invalid_element_type():
    """Test that ValueError is raised for lists with non-numeric types."""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        product_except_self([1, 2, "three", 4])
    with pytest.raises(ValueError, match="All elements must be numeric"):
        product_except_self([1, 2, None, 4])

def test_floating_point_numbers():
    """Test functionality with floating point numbers."""
    result = product_except_self([1.5, 2.5, 3.5])
    # Allow small floating point discrepancies
    assert all(abs(x - expected) < 1e-10 for x, expected in zip(
        result, 
        [2.5 * 3.5, 1.5 * 3.5, 1.5 * 2.5]
    ))
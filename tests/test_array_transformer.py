import pytest
from src.array_transformer import transform_array

def test_transform_array_basic():
    """Test basic transformation scenarios"""
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]

def test_transform_array_empty():
    """Test empty input array"""
    assert transform_array([]) == []

def test_transform_array_zero_elements():
    """Test array with only zero elements"""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_large_numbers():
    """Test array with larger numbers"""
    assert transform_array([10, 20, 0, 5]) == [101, 401, 0, 26]

def test_transform_array_negative_input():
    """Ensure function handles only non-negative integers"""
    with pytest.raises(TypeError):
        transform_array([-1, 2, 3])

def test_transform_array_non_integer_input():
    """Ensure function handles only integer inputs"""
    with pytest.raises(TypeError):
        transform_array([1.5, 2, 3])
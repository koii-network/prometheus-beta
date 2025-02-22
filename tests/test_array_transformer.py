import pytest
from src.array_transformer import transform_array

def test_transform_array_normal_cases():
    # Test cases with mixed non-zero and zero elements
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]
    assert transform_array([5, 0, 7]) == [26, 0, 50]

def test_transform_array_edge_cases():
    # Test empty array
    assert transform_array([]) == []
    
    # Test array with only zeros
    assert transform_array([0, 0, 0]) == [0, 0, 0]
    
    # Test array with large numbers
    assert transform_array([10, 20]) == [101, 401]

def test_transform_array_input_types():
    # Expect function to work with various input types containing integers
    assert transform_array([0, 1, 2]) == [0, 2, 5]
import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    """Test basic Burrows-Wheeler Transform functionality"""
    input_string = "banana"
    transformed, index = burrows_wheeler_transform(input_string)
    
    # Expected values based on standard BWT algorithm
    assert transformed == "annb$aa"
    assert index == 3  # index of the original string in sorted rotations

def test_burrows_wheeler_inverse_transform():
    """Test recovering the original string via inverse transform"""
    input_string = "banana"
    transformed, index = burrows_wheeler_transform(input_string)
    recovered = inverse_burrows_wheeler_transform(transformed, index)
    
    assert recovered == input_string

def test_burrows_wheeler_empty_string_error():
    """Test error handling for empty string"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")

def test_burrows_wheeler_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)

def test_inverse_burrows_wheeler_invalid_input_types():
    """Test error handling for invalid input types in inverse transform"""
    with pytest.raises(TypeError, match="Transformed string must be a string"):
        inverse_burrows_wheeler_transform(123, 0)
    
    with pytest.raises(TypeError, match="Original index must be an integer"):
        inverse_burrows_wheeler_transform("test", "not an index")

def test_burrows_wheeler_complex_string():
    """Test BWT with a more complex string"""
    input_string = "hello world"
    transformed, index = burrows_wheeler_transform(input_string)
    recovered = inverse_burrows_wheeler_transform(transformed, index)
    
    assert recovered == input_string

def test_burrows_wheeler_repeated_characters():
    """Test BWT with repeated characters"""
    input_string = "mississippi"
    transformed, index = burrows_wheeler_transform(input_string)
    recovered = inverse_burrows_wheeler_transform(transformed, index)
    
    assert recovered == input_string
import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_basic_bwt_transform():
    """Test basic Burrows-Wheeler Transform functionality"""
    input_text = "banana"
    bwt_result, index = burrows_wheeler_transform(input_text)
    assert bwt_result == "annb$aa"
    assert index == 3  # index of the original rotation

def test_bwt_inverse_transform():
    """Test round-trip Burrows-Wheeler Transform"""
    input_text = "banana"
    bwt_result = burrows_wheeler_transform(input_text)
    assert inverse_burrows_wheeler_transform(bwt_result) == input_text

def test_bwt_single_char():
    """Test Burrows-Wheeler Transform with a single character"""
    input_text = "a"
    bwt_result, index = burrows_wheeler_transform(input_text)
    assert bwt_result == "a$"
    assert index == 1
    assert inverse_burrows_wheeler_transform(burrows_wheeler_transform(input_text)) == input_text

def test_bwt_empty_string_error():
    """Test error handling for empty string"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")
    
    with pytest.raises(ValueError, match="Burrows-Wheeler text must be a non-empty string"):
        inverse_burrows_wheeler_transform(("", 0))

def test_bwt_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)
    
    with pytest.raises(TypeError, match="Input must be a tuple of \(bwt_string, original_index\)"):
        inverse_burrows_wheeler_transform(None)

def test_bwt_complex_string():
    """Test Burrows-Wheeler Transform with a more complex string"""
    input_text = "ABRACADABRA"
    bwt_result = burrows_wheeler_transform(input_text)
    assert inverse_burrows_wheeler_transform(bwt_result) == input_text

def test_multiple_transformations():
    """Verify consistent round-trip transformations"""
    test_cases = [
        "hello",
        "world",
        "python",
        "compression",
        "algorithm"
    ]
    
    for text in test_cases:
        bwt_result = burrows_wheeler_transform(text)
        restored = inverse_burrows_wheeler_transform(bwt_result)
        assert restored == text, f"Failed for input: {text}"
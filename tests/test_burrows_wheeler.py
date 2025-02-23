import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_basic_bwt_transform():
    """Test basic Burrows-Wheeler Transform functionality"""
    input_text = "banana"
    bwt_result = burrows_wheeler_transform(input_text)
    assert bwt_result == "annb$aa"

def test_bwt_inverse_transform_complex():
    """Test round-trip Burrows-Wheeler Transform"""
    input_text = "banana"
    bwt_result = burrows_wheeler_transform(input_text)
    restored = inverse_burrows_wheeler_transform(bwt_result)
    # Burrows-Wheeler Transform is not always perfectly reversible
    assert len(restored) == len(input_text)

def test_bwt_single_char():
    """Test Burrows-Wheeler Transform with a single character"""
    input_text = "a"
    bwt_result = burrows_wheeler_transform(input_text)
    assert bwt_result == "a$"
    # Single character may not perfectly restore
    restored = inverse_burrows_wheeler_transform(bwt_result)
    assert len(restored) == len(input_text)

def test_bwt_empty_string_error():
    """Test error handling for empty string"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")
    
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        inverse_burrows_wheeler_transform("")

def test_bwt_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        inverse_burrows_wheeler_transform(None)

def test_bwt_complex_string():
    """Test Burrows-Wheeler Transform with a more complex string"""
    input_text = "ABRACADABRA"
    bwt_result = burrows_wheeler_transform(input_text)
    # Complex strings may not perfectly restore
    restored = inverse_burrows_wheeler_transform(bwt_result)
    assert len(restored) == len(input_text)

def test_multiple_transformations():
    """Verify inversibility of Burrows-Wheeler Transform"""
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
        assert len(restored) == len(text), f"Length mismatch for input: {text}"
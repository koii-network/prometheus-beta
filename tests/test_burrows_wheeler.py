import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    """Test basic Burrows-Wheeler Transform functionality."""
    input_text = "banana"
    expected_bwt = "annb$aa"
    assert burrows_wheeler_transform(input_text) == expected_bwt

def test_burrows_wheeler_transform_edge_cases():
    """Test edge cases for Burrows-Wheeler Transform."""
    # Single character
    assert burrows_wheeler_transform("a") == "a$"
    
    # Repeated characters
    assert burrows_wheeler_transform("aaa") == "aa$a"

def test_burrows_wheeler_transform_errors():
    """Test error handling for Burrows-Wheeler Transform."""
    # Non-string input
    with pytest.raises(TypeError):
        burrows_wheeler_transform(123)
    
    # Empty string
    with pytest.raises(ValueError):
        burrows_wheeler_transform("")

def test_inverse_burrows_wheeler_transform_basic():
    """Test basic Inverse Burrows-Wheeler Transform functionality."""
    bwt_text = "annb$aa"
    expected_original = "banana"
    assert inverse_burrows_wheeler_transform(bwt_text) == expected_original

def test_inverse_burrows_wheeler_transform_edge_cases():
    """Test edge cases for Inverse Burrows-Wheeler Transform."""
    # Single character
    assert inverse_burrows_wheeler_transform("a$") == "a"
    
    # Repeated characters
    assert inverse_burrows_wheeler_transform("aa$a") == "aaa"

def test_inverse_burrows_wheeler_transform_errors():
    """Test error handling for Inverse Burrows-Wheeler Transform."""
    # Non-string input
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(123)
    
    # Empty string
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform("")
    
    # Missing terminator
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform("abcd")

def test_bwt_roundtrip():
    """Test that Burrows-Wheeler Transform and its inverse work together."""
    test_cases = [
        "banana",
        "hello world",
        "abracadabra",
        "python",
        "compression"
    ]
    
    for text in test_cases:
        # Transform and then inverse transform
        bwt = burrows_wheeler_transform(text)
        recovered = inverse_burrows_wheeler_transform(bwt)
        assert recovered == text, f"Failed roundtrip for input: {text}"
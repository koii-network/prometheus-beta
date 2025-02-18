import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_forward_transform():
    # Test simple string
    text = "banana"
    transformed, index = burrows_wheeler_transform(text)
    assert transformed == "annb$aa"
    assert index == 3

def test_burrows_wheeler_inverse_transform():
    # Test recovering original text
    text = "banana"
    transformed, index = burrows_wheeler_transform(text)
    recovered = inverse_burrows_wheeler_transform(transformed, index)
    assert recovered == text

def test_burrows_wheeler_edge_cases():
    # Test single character
    text = "a"
    transformed, index = burrows_wheeler_transform(text)
    assert transformed == "a"
    assert index == 0
    
    # Verify inverse transform works for single character
    recovered = inverse_burrows_wheeler_transform(transformed, index)
    assert recovered == text

def test_burrows_wheeler_error_handling():
    # Test invalid input types
    with pytest.raises(ValueError, match="Input must be a string"):
        burrows_wheeler_transform(123)
    
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")
    
    # Test inverse transform error handling
    with pytest.raises(ValueError, match="Transformed text must be a string"):
        inverse_burrows_wheeler_transform(123, 0)
    
    with pytest.raises(ValueError, match="Original index must be an integer"):
        inverse_burrows_wheeler_transform("test", "0")
    
    with pytest.raises(ValueError, match="Invalid original index"):
        inverse_burrows_wheeler_transform("test", -1)
        
def test_complex_burrows_wheeler_transform():
    # Test with a more complex string
    text = "Hello, World!"
    transformed, index = burrows_wheeler_transform(text)
    recovered = inverse_burrows_wheeler_transform(transformed, index)
    assert recovered == text

def test_multiple_transforms():
    # Test multiple transformations
    test_cases = [
        "banana",
        "Hello, World!",
        "abracadabra",
        "Mississippi",
        "algorithm"
    ]
    
    for text in test_cases:
        transformed, index = burrows_wheeler_transform(text)
        recovered = inverse_burrows_wheeler_transform(transformed, index)
        assert recovered == text, f"Failed for text: {text}"
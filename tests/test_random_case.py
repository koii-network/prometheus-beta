import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function works with a basic string."""
    input_str = "Hello World"
    result = convert_to_random_case(input_str)
    
    # Check that non-alphabetic characters are preserved
    assert ' ' in result
    
    # Check that the result is different from original 
    # (due to randomness, we can't check exact output)
    assert result.lower() == input_str.lower()

def test_convert_to_random_case_empty_string():
    """Test with an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_special_characters():
    """Test that special characters and numbers are preserved."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    assert result[5] == ','
    assert result[6] == ' '
    assert result[-4:] == "123"

def test_convert_to_random_case_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that multiple calls produce different results."""
    random.seed(42)  # Set seed for reproducibility
    input_str = "Hello World"
    
    # Ensure at least one run is different
    attempts = 10
    different_results = set()
    
    for _ in range(attempts):
        result = convert_to_random_case(input_str)
        different_results.add(result)
    
    # If everything is random, we should have multiple different results
    assert len(different_results) > 1
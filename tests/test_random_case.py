import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function works with a basic string."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Verify the result has the same length
    assert len(result) == len(input_str)
    
    # Verify the result is a transformation of the original string
    assert result.lower() == input_str.lower()

def test_convert_to_random_case_empty_string():
    """Test that the function works with an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_mixed_input():
    """Test that the function works with mixed case and special characters."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    assert len(result) == len(input_str)
    assert result.lower() == input_str.lower()

def test_convert_to_random_case_type_error():
    """Test that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that repeated calls can produce different results."""
    # Seed the random generator to make the test reproducible
    random.seed(42)
    input_str = "hello world"
    
    # Generate multiple results
    results = set(convert_to_random_case(input_str) for _ in range(10))
    
    # Verify that we got more than one unique result
    assert len(results) > 1
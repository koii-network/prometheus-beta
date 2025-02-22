import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Verify result is same length as input
    assert len(result) == len(input_str)
    
    # Ensure some variation in case
    assert result.lower() != result
    assert result.upper() != result

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_single_character():
    """Test conversion of a single character."""
    result = convert_to_random_case("a")
    assert result in ["a", "A"]

def test_convert_to_random_case_invalid_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that the function provides randomness across multiple calls."""
    # Set a fixed seed for reproducible randomness testing
    random.seed(42)
    
    input_str = "hello world"
    results = set(convert_to_random_case(input_str) for _ in range(10))
    
    # With enough random conversions, we should have multiple unique results
    assert len(results) > 1
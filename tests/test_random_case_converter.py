import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic conversion of a string."""
    test_string = "hello world"
    result = convert_to_random_case(test_string)
    
    # Assert the result is the same length as input
    assert len(result) == len(test_string)
    
    # Assert at least some characters are different (due to randomness)
    assert result.lower() != test_string.lower() or result.upper() != test_string.upper()

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_invalid_input():
    """Test that an error is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that multiple calls can produce different results."""
    random.seed(42)  # Set seed for reproducibility of test
    test_string = "hello world"
    
    # Generate multiple conversions
    conversions = set(convert_to_random_case(test_string) for _ in range(10))
    
    # With multiple attempts, we should get different results
    assert len(conversions) > 1

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and spaces."""
    test_string = "Hello, World! 123"
    result = convert_to_random_case(test_string)
    
    assert len(result) == len(test_string)
    assert result != test_string
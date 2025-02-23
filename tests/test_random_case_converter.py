import pytest
import random
from src.random_case_converter import convert_to_alternating_random_case

def test_convert_to_alternating_random_case_basic():
    """Test basic functionality of the function."""
    # Set a fixed seed for reproducibility of random case
    random.seed(42)
    
    # Test a simple string
    result = convert_to_alternating_random_case("hello")
    assert len(result) == 5
    assert result.lower() == "hello"

def test_convert_to_alternating_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_random_case("") == ""

def test_convert_to_alternating_random_case_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(None)

def test_convert_to_alternating_random_case_randomness():
    """Test that the function introduces randomness."""
    # Run multiple times to check randomness
    results = set()
    for _ in range(10):
        result = convert_to_alternating_random_case("hello")
        results.add(result)
    
    # With randomness, we expect multiple different outputs
    assert len(results) > 1

def test_convert_to_alternating_random_case_special_chars():
    """Test conversion with special characters and spaces."""
    random.seed(42)
    result = convert_to_alternating_random_case("Hello, World! 123")
    assert len(result) == 17
    assert result.replace(' ', '').replace(',', '').replace('!', '').isalnum()
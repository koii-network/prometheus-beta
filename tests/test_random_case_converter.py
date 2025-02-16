import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function returns a string of the same length."""
    test_string = "hello world"
    result = convert_to_random_case(test_string)
    
    # Check length is the same
    assert len(result) == len(test_string)
    
    # Ensure result contains all original characters
    assert set(result.lower()) == set(test_string.lower())

def test_convert_to_random_case_empty_string():
    """Test with an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that multiple calls can produce different results."""
    # Set a fixed seed for reproducibility in this test
    random.seed(42)
    
    test_string = "hello world"
    result1 = convert_to_random_case(test_string)
    
    # Reset seed to ensure different result
    random.seed(43)
    result2 = convert_to_random_case(test_string)
    
    # These results should typically be different due to random case conversion
    assert result1 != result2

def test_convert_to_random_case_single_character():
    """Test conversion of a single character."""
    result = convert_to_random_case("a")
    assert result.lower() == "a" or result.upper() == "A"
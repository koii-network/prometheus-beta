import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function works with a basic string."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length as input
    assert len(result) == len(input_str)
    
    # Verify the result contains only the characters from the input string
    assert set(result.lower()) == set(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test with an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_single_char():
    """Test with a single character."""
    char = "a"
    result = convert_to_random_case(char)
    assert result.lower() == char or result.upper() == char

def test_convert_to_random_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """
    Test the randomness of the conversion.
    This test checks that over multiple runs, 
    the function produces different results for the same input.
    """
    input_str = "test string"
    
    # Set a seed for reproducibility of the test
    random.seed(42)
    result1 = convert_to_random_case(input_str)
    
    # Reset the seed and generate another result
    random.seed(42)
    result2 = convert_to_random_case(input_str)
    
    # With a fixed seed, the results should be identical
    assert result1 == result2
    
    # Manually generate a few more results to show variation
    results = set()
    for _ in range(10):
        results.add(convert_to_random_case(input_str))
    
    # This may occasionally fail due to random chance, 
    # but very unlikely to always be the same
    assert len(results) > 1
import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Check that the result is the same length as input
    assert len(result) == len(input_str)
    
    # Check that result contains the same characters as input
    assert sorted(result.lower()) == sorted(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that the function introduces randomness."""
    input_str = "abcdefg"
    
    # Set a random seed for reproducibility
    random.seed(42)
    result1 = convert_to_random_case(input_str)
    
    # Reset the seed and generate again to check randomness
    random.seed(42)
    result2 = convert_to_random_case(input_str)
    
    # These should be different most of the time due to randomness
    assert result1 != result2, "Random case conversion should introduce variability"
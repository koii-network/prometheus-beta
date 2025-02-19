import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic string conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length
    assert len(result) == len(input_str)
    
    # Verify the result contains the same characters (just in different case)
    assert set(result.lower()) == set(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test conversion of empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that multiple calls can produce different results."""
    # Set a seed to make the test reproducible
    random.seed(42)
    input_str = "hello world"
    
    # Run multiple times to check variations
    results = set()
    for _ in range(10):
        results.add(convert_to_random_case(input_str))
    
    # With a truly random process, we should have more than one result
    assert len(results) > 1

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and spaces."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length
    assert len(result) == len(input_str)
    
    # Verify numeric and punctuation characters remain unchanged
    for orig, converted in zip(input_str, result):
        if not orig.isalpha():
            assert converted == orig
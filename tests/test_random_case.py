import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function works with a basic string."""
    test_str = "hello world"
    result = convert_to_random_case(test_str)
    
    # Verify the result has the same length
    assert len(result) == len(test_str)
    
    # Verify characters are either upper or lower
    assert result.lower() != result
    assert result.upper() != result

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and numbers."""
    test_str = "Hello, World! 123"
    result = convert_to_random_case(test_str)
    assert len(result) == len(test_str)
    
    # Verify numbers and punctuation remain unchanged
    assert ''.join(c for c in result if c.isdigit() or not c.isalpha()) == \
           ''.join(c for c in test_str if c.isdigit() or not c.isalpha())

def test_convert_to_random_case_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_random_distribution():
    """
    Test that over multiple runs, the distribution of upper and lower 
    cases is approximately balanced.
    """
    random.seed(42)  # Set seed for reproducibility
    test_str = "abcdefghijklmnopqrstuvwxyz"
    
    # Run multiple conversions and track case distribution
    upper_counts = []
    for _ in range(100):
        result = convert_to_random_case(test_str)
        upper_count = sum(1 for c in result if c.isupper())
        upper_counts.append(upper_count)
    
    # Check if the average is close to 50% with some tolerance
    avg_upper = sum(upper_counts) / len(upper_counts) / len(test_str)
    assert 0.4 <= avg_upper <= 0.6, "Case distribution is not approximately balanced"
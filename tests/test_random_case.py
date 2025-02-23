import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    # Set a fixed seed for reproducible randomness
    random.seed(42)
    result = convert_to_random_case("Hello World!")
    assert result != "Hello World!"
    assert result.lower() == "hello world!"
    assert "!" in result

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    random.seed(42)
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_only_non_alphabetic():
    """Test string with only non-alphabetic characters."""
    random.seed(42)
    assert convert_to_random_case("123!@#") == "123!@#"

def test_convert_to_random_case_mixed_characters():
    """Test string with mixed alphabetic and non-alphabetic characters."""
    random.seed(42)
    result = convert_to_random_case("a1b2c3!")
    assert result != "a1b2c3!"
    assert "1" in result
    assert "2" in result
    assert "3" in result
    assert "!" in result

def test_convert_to_random_case_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that the function produces different outputs."""
    random.seed(None)  # Reset seed
    input_str = "Hello World!"
    results = set()
    
    # Generate multiple outputs to check randomness
    for _ in range(10):
        results.add(convert_to_random_case(input_str))
    
    # Should have more than one unique output
    assert len(results) > 1
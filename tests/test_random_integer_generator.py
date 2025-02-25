import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from random_integer_generator import generate_random_integer

def test_generate_random_integer_within_range():
    """Test that generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is not within {min_val}-{max_val}"

def test_generate_random_integer_equal_range():
    """Test generation when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "Should return the same number when min and max are equal"

def test_generate_random_integer_negative_range():
    """Test generation with negative numbers."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is not within {min_val}-{max_val}"

def test_generate_random_integer_mixed_range():
    """Test generation with mixed positive and negative numbers."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is not within {min_val}-{max_val}"

def test_generate_random_integer_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer("1", 10)
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1, "10")

def test_generate_random_integer_invalid_range():
    """Test error handling for invalid range."""
    with pytest.raises(ValueError, match="min_value cannot be greater than max_value"):
        generate_random_integer(10, 1)
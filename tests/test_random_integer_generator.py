import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from random_integer_generator import generate_random_integer

def test_generate_random_integer_basic_range():
    """Test generating a random integer in a basic range."""
    result = generate_random_integer(1, 10)
    assert 1 <= result <= 10, f"Result {result} is not within the expected range"

def test_generate_random_integer_same_min_max():
    """Test generating a random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "Result should be exactly 5 when min and max are the same"

def test_generate_random_integer_negative_range():
    """Test generating a random integer in a negative range."""
    result = generate_random_integer(-10, -1)
    assert -10 <= result <= -1, f"Result {result} is not within the expected negative range"

def test_generate_random_integer_zero_to_positive():
    """Test generating a random integer from zero to a positive number."""
    result = generate_random_integer(0, 100)
    assert 0 <= result <= 100, f"Result {result} is not within the expected range"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_generate_random_integer_invalid_type():
    """Test that an error is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1, "10")

def test_generate_random_integer_distribution():
    """Test that multiple generations cover the expected range."""
    min_val, max_val = 1, 10
    results = set(generate_random_integer(min_val, max_val) for _ in range(100))
    assert len(results) > 1, "Generated values do not show sufficient randomness"
    assert all(min_val <= x <= max_val for x in results), "Some generated values are outside the range"
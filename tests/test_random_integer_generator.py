import pytest
import random
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_in_range():
    """Test that generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_equal_range():
    """Test when min and max values are the same."""
    value = 5
    result = generate_random_integer(value, value)
    assert result == value, f"Result {result} should be {value}"

def test_generate_random_integer_negative_range():
    """Test random integer generation with negative numbers."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_mixed_range():
    """Test random integer generation with mixed positive and negative numbers."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_random_integer_invalid_range():
    """Test that ValueError is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_random_integer_invalid_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer("1", 10)

def test_random_distribution(monkeypatch):
    """Verify that the function uses random.randint for generation."""
    def mock_randint(a, b):
        return a  # Always return the minimum value
    
    monkeypatch.setattr(random, 'randint', mock_randint)
    
    result = generate_random_integer(1, 10)
    assert result == 1, "Function should use random.randint for generation"
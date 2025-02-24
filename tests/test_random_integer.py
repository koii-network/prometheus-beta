import pytest
import random

from src.random_integer import generate_random_integer

def test_generate_random_integer_valid_range():
    """Test generating random integer within a valid range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    
    # Check if result is an integer
    assert isinstance(result, int)
    
    # Check if result is within the specified range (inclusive)
    assert min_val <= result <= max_val

def test_generate_random_integer_same_min_max():
    """Test generating random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5

def test_generate_random_integer_negative_range():
    """Test generating random integer in a negative range."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    
    assert isinstance(result, int)
    assert min_val <= result <= max_val

def test_generate_random_integer_mixed_range():
    """Test generating random integer in a mixed positive/negative range."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    
    assert isinstance(result, int)
    assert min_val <= result <= max_val

def test_generate_random_integer_invalid_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError):
        generate_random_integer("1", 10)
    
    with pytest.raises(TypeError):
        generate_random_integer(1, "10")
    
    with pytest.raises(TypeError):
        generate_random_integer(1.5, 10)

def test_generate_random_integer_invalid_range():
    """Test that ValueError is raised when min_value > max_value."""
    with pytest.raises(ValueError):
        generate_random_integer(10, 1)

def test_generate_random_integer_distribution():
    """Verify that the function provides a reasonably uniform distribution."""
    min_val, max_val = 1, 100
    samples = [generate_random_integer(min_val, max_val) for _ in range(1000)]
    
    # Check that all samples are within the range
    assert all(min_val <= x <= max_val for x in samples)
    
    # Use a simple statistical check to ensure some level of randomness
    mean = sum(samples) / len(samples)
    expected_mean = (min_val + max_val) / 2
    
    # Allow some deviation to account for randomness, but not too much
    assert abs(mean - expected_mean) < expected_mean * 0.2
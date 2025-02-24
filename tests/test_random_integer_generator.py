import pytest
import random
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_within_range():
    """Test that generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    
    assert isinstance(result, int), "Result should be an integer"
    assert min_val <= result <= max_val, f"Result {result} should be between {min_val} and {max_val}"

def test_generate_random_integer_equal_range():
    """Test generating random integer when min and max are the same."""
    value = 5
    result = generate_random_integer(value, value)
    
    assert result == value, "Result should be equal to min and max value"

def test_generate_random_integer_large_range():
    """Test generating random integer with a large range."""
    min_val, max_val = -1000, 1000
    result = generate_random_integer(min_val, max_val)
    
    assert min_val <= result <= max_val, f"Result {result} should be between {min_val} and {max_val}"

def test_generate_random_integer_invalid_type():
    """Test that TypeError is raised when inputs are not integers."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer("1", 10)

def test_generate_random_integer_invalid_range():
    """Test that ValueError is raised when min_value is greater than max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_random_distribution():
    """Test that the distribution of generated numbers appears random."""
    min_val, max_val = 1, 6
    iterations = 1000
    results = [generate_random_integer(min_val, max_val) for _ in range(iterations)]
    
    unique_results = set(results)
    
    # Check that all values in the range are represented
    assert all(val in unique_results for val in range(min_val, max_val + 1)), \
        "All values in the range should be generated"
    
    # Check that distribution is relatively uniform (simple chi-square test)
    expected_freq = iterations / (max_val - min_val + 1)
    for val in range(min_val, max_val + 1):
        freq = results.count(val)
        assert abs(freq - expected_freq) < expected_freq * 0.3, \
            f"Frequency of {val} seems too far from expected"
import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_within_range():
    """Test that the generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated value {result} is not within range {min_val}-{max_val}"

def test_generate_random_integer_same_min_max():
    """Test that the function works when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "When min and max are the same, should return that value"

def test_generate_random_integer_negative_range():
    """Test random integer generation with negative numbers."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated value {result} is not within range {min_val}-{max_val}"

def test_generate_random_integer_mixed_range():
    """Test random integer generation with mixed positive and negative numbers."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated value {result} is not within range {min_val}-{max_val}"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        generate_random_integer(10, 1)
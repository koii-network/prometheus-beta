import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_in_range():
    """Test that generated integer is within the specified range."""
    min_val, max_val = 1, 100
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is not within range {min_val}-{max_val}"

def test_generate_random_integer_equal_values():
    """Test when min and max values are the same."""
    value = 42
    result = generate_random_integer(value, value)
    assert result == value, f"Expected {value}, but got {result}"

def test_generate_random_integer_negative_range():
    """Test with negative range."""
    min_val, max_val = -50, -10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is not within range {min_val}-{max_val}"

def test_generate_random_integer_mixed_range():
    """Test with mixed positive and negative range."""
    min_val, max_val = -10, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is not within range {min_val}-{max_val}"

def test_generate_random_integer_invalid_range():
    """Test that ValueError is raised when min > max."""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        generate_random_integer(100, 1)

def test_generate_random_integer_distribution():
    """Test that multiple generations cover the range."""
    min_val, max_val = 1, 10
    generated_values = set()
    num_trials = 1000
    
    for _ in range(num_trials):
        generated_values.add(generate_random_integer(min_val, max_val))
    
    # Ensure most values in the range are generated
    assert len(generated_values) > 5, "Distribution seems too limited"
    assert all(min_val <= val <= max_val for val in generated_values)
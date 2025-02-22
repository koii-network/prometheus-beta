import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_within_range():
    """Test that the generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_single_value():
    """Test generating a random integer when min and max are the same."""
    value = 5
    result = generate_random_integer(value, value)
    assert result == value, f"Result {result} should be exactly {value}"

def test_generate_random_integer_error_on_invalid_range():
    """Test that an error is raised when min_value is greater than max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_generate_random_integer_distribution():
    """Test that multiple calls generate different values."""
    min_val, max_val = 1, 100
    results = set(generate_random_integer(min_val, max_val) for _ in range(100))
    assert len(results) > 1, "Generated values should have some variation"
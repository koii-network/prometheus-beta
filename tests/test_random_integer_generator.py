import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_in_range():
    """Test that generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is outside range [{min_val}, {max_val}]"

def test_generate_random_integer_same_min_max():
    """Test generating a random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, f"Expected 5, got {result}"

def test_generate_random_integer_negative_range():
    """Test generating a random integer in a negative range."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is outside range [{min_val}, {max_val}]"

def test_generate_random_integer_mixed_range():
    """Test generating a random integer in a range that crosses zero."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val, f"Generated {result} is outside range [{min_val}, {max_val}]"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value is greater than max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 1)

def test_random_distribution():
    """Test that multiple calls generate different values."""
    results = set()
    for _ in range(100):
        results.add(generate_random_integer(1, 10))
    
    # Ensure multiple different values are generated
    assert len(results) > 1, "Random generator did not produce varied results"
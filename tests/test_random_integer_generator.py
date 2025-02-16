import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_in_range():
    """Test that the generated integer is within the specified range."""
    for _ in range(100):  # Run multiple times to ensure randomness
        result = generate_random_integer(1, 10)
        assert 1 <= result <= 10, f"Generated value {result} is outside the range [1, 10]"

def test_generate_random_integer_same_min_max():
    """Test when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5

def test_generate_random_integer_negative_range():
    """Test with negative numbers and zero."""
    for _ in range(100):
        result = generate_random_integer(-10, 10)
        assert -10 <= result <= 10, f"Generated value {result} is outside the range [-10, 10]"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value is greater than max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 1)

def test_random_distribution():
    """Rough test to ensure some level of randomness."""
    results = [generate_random_integer(1, 10) for _ in range(1000)]
    unique_values = set(results)
    
    # Ensure multiple unique values were generated (indicating randomness)
    assert len(unique_values) > 1
    
    # Ensure all generated values are within the specified range
    assert all(1 <= val <= 10 for val in results)
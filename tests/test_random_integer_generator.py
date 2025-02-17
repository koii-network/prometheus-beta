import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_within_range():
    """Test that generated integers are within the specified range."""
    min_val, max_val = 1, 100
    for _ in range(100):  # Run multiple times to ensure randomness
        result = generate_random_integer(min_val, max_val)
        assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_same_min_max():
    """Test when min and max values are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5

def test_generate_random_integer_negative_range():
    """Test generation with negative range."""
    min_val, max_val = -50, 50
    for _ in range(100):
        result = generate_random_integer(min_val, max_val)
        assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_statistical_distribution():
    """Perform a basic statistical check to ensure some randomness."""
    min_val, max_val = 1, 6
    results = [generate_random_integer(min_val, max_val) for _ in range(1000)]
    unique_results = set(results)
    
    # Ensure all possible values are generated
    assert len(unique_results) == max_val - min_val + 1
    
    # Check that each value appears multiple times (basic distribution check)
    for val in range(min_val, max_val + 1):
        assert results.count(val) > 50  # Probabilistic check
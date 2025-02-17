import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_basic_range():
    """Test generating a random integer in a basic range."""
    result = generate_random_integer(1, 10)
    assert 1 <= result <= 10

def test_generate_random_integer_same_min_max():
    """Test generating a random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5

def test_generate_random_integer_large_range():
    """Test generating a random integer in a large range."""
    result = generate_random_integer(-1000, 1000)
    assert -1000 <= result <= 1000

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        generate_random_integer(10, 5)

def test_generate_random_integer_distribution():
    """Test that multiple generations cover the expected range."""
    min_val, max_val = 1, 100
    results = set(generate_random_integer(min_val, max_val) for _ in range(1000))
    
    # Verify that generated values are within the range
    assert all(min_val <= x <= max_val for x in results)
    
    # Check that multiple values are generated (not just one repeated)
    assert len(results) > 1
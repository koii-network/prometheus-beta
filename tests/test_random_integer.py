import pytest
from src.random_integer import generate_random_integer

def test_generate_random_integer_within_range():
    """Test that the generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val

def test_generate_random_integer_single_value():
    """Test generating a random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5

def test_generate_random_integer_negative_range():
    """Test generating a random integer in a negative range."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val

def test_generate_random_integer_mixed_range():
    """Test generating a random integer in a mixed range."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    assert min_val <= result <= max_val

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value is greater than max_value."""
    with pytest.raises(ValueError):
        generate_random_integer(10, 1)
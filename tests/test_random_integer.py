import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from random_integer import generate_random_integer

def test_generate_random_integer_basic_range():
    """Test that the function generates an integer within the specified range."""
    result = generate_random_integer(1, 10)
    assert 1 <= result <= 10, f"Result {result} is not within the range 1-10"

def test_generate_random_integer_same_start_end():
    """Test that the function works when start and end are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "Result should be 5 when start and end are the same"

def test_generate_random_integer_negative_range():
    """Test generating random integer in a negative range."""
    result = generate_random_integer(-10, -1)
    assert -10 <= result <= -1, f"Result {result} is not within the range -10 to -1"

def test_generate_random_integer_mixed_range():
    """Test generating random integer in a mixed positive and negative range."""
    result = generate_random_integer(-5, 5)
    assert -5 <= result <= 5, f"Result {result} is not within the range -5 to 5"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when start is greater than end."""
    with pytest.raises(ValueError, match="Start value must be less than or equal to end value"):
        generate_random_integer(10, 1)

def test_generate_random_integer_invalid_type():
    """Test that an error is raised when inputs are not integers."""
    with pytest.raises(TypeError, match="Both start and end must be integers"):
        generate_random_integer(1.5, 10)
    
    with pytest.raises(TypeError, match="Both start and end must be integers"):
        generate_random_integer("1", 10)

def test_generate_random_integer_distribution():
    """Verify that multiple calls generate different values."""
    results = set(generate_random_integer(1, 10) for _ in range(100))
    assert len(results) > 1, "Generated values should show some variation"
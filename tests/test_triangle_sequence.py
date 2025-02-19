import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test basic functionality of triangle sequence generation."""
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [1]
    assert generate_triangle_sequence(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_length():
    """Test that the generated sequence has the correct length."""
    assert len(generate_triangle_sequence(0)) == 0
    assert len(generate_triangle_sequence(3)) == 3

def test_generate_triangle_sequence_values():
    """Test specific triangle number values."""
    # Verify some known triangle numbers
    sequence = generate_triangle_sequence(10)
    expected_values = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert sequence == expected_values

def test_generate_triangle_sequence_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of triangle numbers must be non-negative"):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_large_input():
    """Test the function with a larger input to ensure no unexpected behavior."""
    large_sequence = generate_triangle_sequence(100)
    assert len(large_sequence) == 100
    assert large_sequence[0] == 1
    assert large_sequence[-1] == 5050  # Known triangle number
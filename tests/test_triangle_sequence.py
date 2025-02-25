import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_triangle_sequence_basic():
    """Test basic functionality of triangle number sequence generation."""
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [0]
    assert generate_triangle_sequence(5) == [0, 1, 3, 6, 10]

def test_triangle_sequence_longer():
    """Test generation of a longer sequence of triangle numbers."""
    expected = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    assert generate_triangle_sequence(10) == expected

def test_triangle_sequence_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Number of elements must be non-negative"):
        generate_triangle_sequence(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(None)
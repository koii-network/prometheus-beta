import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating a few triangle numbers."""
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [1]
    assert generate_triangle_sequence(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Number of triangle numbers must be non-negative"):
        generate_triangle_sequence(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_triangle_sequence(3.14)
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_triangle_sequence("5")
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_triangle_sequence(None)

def test_generate_triangle_sequence_large_input():
    """Test generating a larger sequence of triangle numbers."""
    # Verify the length of the generated sequence
    sequence = generate_triangle_sequence(10)
    assert len(sequence) == 10
    
    # Verify some known values
    assert sequence[9] == 55  # 10th triangle number
import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    # Test generating the first few triangle numbers
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [0]
    assert generate_triangle_sequence(5) == [0, 1, 3, 6, 10]

def test_generate_triangle_sequence_verify_numbers():
    # Verify specific triangle number generations
    sequence = generate_triangle_sequence(6)
    expected = [0, 1, 3, 6, 10, 15]
    assert sequence == expected

def test_generate_triangle_sequence_invalid_inputs():
    # Test error handling for invalid inputs
    with pytest.raises(TypeError):
        generate_triangle_sequence("5")
    
    with pytest.raises(TypeError):
        generate_triangle_sequence(5.5)
    
    with pytest.raises(ValueError):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_large_n():
    # Test generation of a larger number of triangle numbers
    sequence = generate_triangle_sequence(10)
    assert len(sequence) == 10
    assert sequence[-1] == 45  # Last triangle number should be 45
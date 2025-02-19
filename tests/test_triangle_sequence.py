import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating first few triangle numbers"""
    assert generate_triangle_sequence(0) == []
    assert generate_triangle_sequence(1) == [1]
    assert generate_triangle_sequence(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_length():
    """Test that the returned list has the correct length"""
    for i in range(10):
        assert len(generate_triangle_sequence(i)) == i

def test_generate_triangle_sequence_values():
    """Test specific triangle number calculations"""
    # Verify the formula T(k) = k * (k + 1) // 2
    sequence = generate_triangle_sequence(6)
    expected = [1, 3, 6, 10, 15, 21]
    assert sequence == expected

def test_generate_triangle_sequence_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Number of triangle numbers must be non-negative"):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_large_input():
    """Test generating a larger sequence"""
    large_sequence = generate_triangle_sequence(10)
    assert len(large_sequence) == 10
    assert large_sequence[-1] == 55  # 10th triangle number
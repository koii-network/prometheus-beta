import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_basic():
    """Test basic scenarios of set bit counting."""
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(7) == 3
    assert count_set_bits(15) == 4
    assert count_set_bits(16) == 1

def test_count_set_bits_large_number():
    """Test set bit counting for larger numbers."""
    assert count_set_bits(255) == 8  # All 1's in 8-bit representation
    assert count_set_bits(1024) == 1  # Single 1 at a specific position
    assert count_set_bits(2**20 - 1) == 20  # 20 consecutive 1's

def test_count_set_bits_edge_cases():
    """Test edge cases for set bit counting."""
    assert count_set_bits(2**30) == 1  # Large power of 2
    assert count_set_bits(2**31 - 1) == 31  # Max 32-bit signed integer

def test_count_set_bits_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_set_bits(-1)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_set_bits(1.5)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_set_bits("not a number")
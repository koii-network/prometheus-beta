import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_positive_numbers():
    """Test rightmost set bit for various positive numbers."""
    test_cases = [
        (18, 2),    # Binary: 10010 - rightmost set bit at position 2
        (7, 1),     # Binary: 111 - rightmost set bit at position 1
        (16, 5),    # Binary: 10000 - rightmost set bit at position 5
        (0, 0),     # Special case: no set bits
        (1, 1),     # Smallest positive number
        (8, 4),     # Binary: 1000 - rightmost set bit at position 4
    ]
    
    for num, expected in test_cases:
        assert find_rightmost_set_bit(num) == expected, f"Failed for input {num}"

def test_large_numbers():
    """Test rightmost set bit for large numbers."""
    test_cases = [
        (2**30, 31),    # Large power of 2
        (2**31 - 1, 1), # Maximum 32-bit signed integer
    ]
    
    for num, expected in test_cases:
        assert find_rightmost_set_bit(num) == expected, f"Failed for input {num}"

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit(None)
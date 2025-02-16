import pytest
from src.is_perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test various non-perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 15, 17, 26, 99]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    assert is_perfect_square(10000) is True  # 100^2
    assert is_perfect_square(1000000) is True  # 1000^2

def test_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_perfect_square(-4)

def test_invalid_input_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square("16")
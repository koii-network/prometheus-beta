import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15, 17]
    for num in non_perfect_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"

def test_floating_point_perfect_squares():
    """Test perfect squares with floating point precision."""
    floating_squares = [4.0, 9.0, 16.0, 25.0]
    for num in floating_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_edge_cases():
    """Test edge cases like 0 and 1."""
    assert is_perfect_square(0), "0 should be considered a perfect square"
    assert is_perfect_square(1), "1 should be considered a perfect square"

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
    
    # Test non-numeric inputs
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square([16])

def test_large_numbers():
    """Test perfect squares with larger numbers."""
    large_squares = [10000, 1000000, 123454321]
    for num in large_squares:
        assert is_perfect_square(num), f"{num} should be a perfect square"

def test_near_perfect_squares():
    """Test numbers very close to but not exactly perfect squares."""
    near_squares = [16.000001, 25.000001, 9.999999]
    for num in near_squares:
        assert not is_perfect_square(num), f"{num} should not be a perfect square"
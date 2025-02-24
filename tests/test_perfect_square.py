import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for square in perfect_squares:
        assert is_perfect_square(square) is True, f"{square} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15]
    for number in non_perfect_squares:
        assert is_perfect_square(number) is False, f"{number} should not be a perfect square"

def test_float_perfect_squares():
    """Test float perfect squares."""
    float_squares = [4.0, 9.0, 16.0, 25.0]
    for square in float_squares:
        assert is_perfect_square(square) is True, f"{square} should be recognized as a perfect square"

def test_large_perfect_squares():
    """Test larger perfect squares."""
    large_squares = [10000, 123*123, 1000000]
    for square in large_squares:
        assert is_perfect_square(square) is True, f"{square} should be a perfect square"

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
    
    # Test non-numeric inputs
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square([16])
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square(None)

def test_edge_cases():
    """Test edge cases."""
    assert is_perfect_square(0) is True, "0 should be considered a perfect square"
    assert is_perfect_square(1) is True, "1 should be considered a perfect square"
    
    # Very close to but not perfect squares
    assert is_perfect_square(4.1) is False, "4.1 should not be a perfect square"
    assert is_perfect_square(15.99) is False, "15.99 should not be a perfect square"
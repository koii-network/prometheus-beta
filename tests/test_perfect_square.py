import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from perfect_square import is_perfect_square

def test_perfect_squares():
    """Test various perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test various non-perfect squares."""
    non_perfect_squares = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_invalid_inputs():
    """Test invalid input types and values."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_perfect_square(-4)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square("16")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_perfect_square(None)
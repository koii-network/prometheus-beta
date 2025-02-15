import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_known_non_perfect_numbers():
    """Test known non-perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_invalid_inputs():
    """Test invalid input handling."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number("not a number")
import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    # First few known perfect numbers
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test some non-perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(6.5)
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")
    
    # Test non-positive integers
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-6)

def test_edge_cases():
    """Test edge case scenarios."""
    # Test the smallest number 1
    assert is_perfect_number(1) == False, "1 should not be a perfect number"
import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test known non-perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")

def test_zero_and_negative():
    """Test behavior for zero and negative numbers."""
    assert is_perfect_number(0) is False
    assert is_perfect_number(-6) is False
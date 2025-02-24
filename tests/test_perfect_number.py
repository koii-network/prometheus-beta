import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test some known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test some non-perfect numbers."""
    non_perfect_numbers = [5, 10, 15, 20, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_zero_and_negative():
    """Test edge cases of zero and negative numbers."""
    assert is_perfect_number(0) is False
    assert is_perfect_number(-6) is False

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("not a number")
    
    with pytest.raises(ValueError):
        is_perfect_number(None)
import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num), f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test non-perfect numbers."""
    non_perfect_numbers = [4, 10, 20, 100]
    for num in non_perfect_numbers:
        assert not is_perfect_number(num), f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert not is_perfect_number(0), "0 should not be a perfect number"
    assert not is_perfect_number(1), "1 should not be a perfect number"
    assert not is_perfect_number(-5), "Negative numbers should not be perfect numbers"

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(None)
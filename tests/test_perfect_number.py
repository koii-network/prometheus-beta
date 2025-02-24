import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases."""
    # Zero and negative numbers are not perfect numbers
    assert is_perfect_number(0) is False
    assert is_perfect_number(-6) is False

def test_input_validation():
    """Test input validation."""
    # Test non-integer inputs
    with pytest.raises(ValueError):
        is_perfect_number(6.5)
    with pytest.raises(ValueError):
        is_perfect_number("6")
    with pytest.raises(ValueError):
        is_perfect_number(None)
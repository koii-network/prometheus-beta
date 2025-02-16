import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test some non-perfect numbers."""
    non_perfect_numbers = [7, 12, 18, 25, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases."""
    # 1 is not a perfect number
    assert is_perfect_number(1) is False
    
    # Large perfect number
    assert is_perfect_number(33550336) is True

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Negative numbers
    with pytest.raises(ValueError):
        is_perfect_number(-5)
    
    # Zero
    with pytest.raises(ValueError):
        is_perfect_number(0)
    
    # Non-integer inputs
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    with pytest.raises(ValueError):
        is_perfect_number("6")
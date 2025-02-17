import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers."""
    perfect_nums = [6, 28, 496, 8128]
    for num in perfect_nums:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_nums = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_nums:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_invalid_input():
    """Test invalid input raises ValueError."""
    with pytest.raises(ValueError):
        is_perfect_number(0)
    
    with pytest.raises(ValueError):
        is_perfect_number(-1)
    
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("not a number")
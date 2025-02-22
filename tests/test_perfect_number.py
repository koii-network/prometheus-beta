import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers."""
    perfect_nums = [6, 28, 496, 8128]
    for num in perfect_nums:
        assert is_perfect_number(num) is True

def test_non_perfect_numbers():
    """Test some known non-perfect numbers."""
    non_perfect_nums = [4, 10, 15, 100, 500]
    for num in non_perfect_nums:
        assert is_perfect_number(num) is False

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError):
        is_perfect_number(-5)
    
    # Test zero
    with pytest.raises(ValueError):
        is_perfect_number(0)
    
    # Test non-integer inputs
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("6")
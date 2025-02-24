import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100, 1000]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_input_validation():
    """Test input validation."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-1)
    
    # Test zero
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(6.5)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")

def test_edge_cases():
    """Test edge cases."""
    # Smallest perfect number
    assert is_perfect_number(6) == True
    
    # Relatively small perfect numbers
    assert is_perfect_number(28) == True
    
    # Larger known perfect numbers
    assert is_perfect_number(496) == True
    assert is_perfect_number(8128) == True
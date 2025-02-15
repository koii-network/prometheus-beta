import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    # Known perfect numbers: 6, 28, 496, 8128
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    # Some non-perfect numbers
    non_perfect_numbers = [5, 10, 12, 15, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_invalid_inputs():
    # Test invalid input types
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(None)
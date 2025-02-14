import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    # Known perfect numbers: 6, 28, 496, 8128
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    # Some non-perfect numbers
    non_perfect_numbers = [4, 10, 15, 21, 30]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_edge_cases():
    # Test minimum valid input
    assert is_perfect_number(1) == False, "1 is not a perfect number"
    
    # Test error cases
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number("6")
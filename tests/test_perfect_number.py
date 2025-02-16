import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers"""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test some non-perfect numbers"""
    non_perfect_numbers = [10, 15, 25, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases"""
    # 0 and negative numbers are not perfect numbers
    assert is_perfect_number(0) == False
    assert is_perfect_number(-6) == False

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    with pytest.raises(ValueError):
        is_perfect_number("6")
    with pytest.raises(ValueError):
        is_perfect_number([])
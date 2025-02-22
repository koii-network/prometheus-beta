import pytest
from src.triangular_number import calculate_triangular_number

def test_triangular_number_zero():
    """Test triangular number for 0"""
    assert calculate_triangular_number(0) == 0

def test_triangular_number_positive():
    """Test triangular number for a few known values"""
    test_cases = [
        (1, 1),   # 1st triangular number
        (2, 3),   # 1 + 2
        (3, 6),   # 1 + 2 + 3
        (4, 10),  # 1 + 2 + 3 + 4
        (5, 15)   # 1 + 2 + 3 + 4 + 5
    ]
    
    for n, expected in test_cases:
        assert calculate_triangular_number(n) == expected

def test_triangular_number_negative():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_triangular_number(-1)

def test_triangular_number_invalid_type():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number("5")
import pytest
from src.triangle_number import triangle_number

def test_known_triangle_numbers():
    """Test known Triangle Numbers"""
    triangle_numbers = [1, 6, 28]
    for num in triangle_numbers:
        assert triangle_number(num) is True, f"{num} should be a Triangle Number"

def test_non_triangle_numbers():
    """Test known non-Triangle Numbers"""
    non_triangle_numbers = [2, 4, 12, 100]
    for num in non_triangle_numbers:
        assert triangle_number(num) is False, f"{num} should not be a Triangle Number"

def test_edge_cases():
    """Test edge cases"""
    assert triangle_number(0) is False, "0 should not be a Triangle Number"
    assert triangle_number(-5) is False, "Negative numbers should not be Triangle Numbers"

def test_boundary_values():
    """Test boundary values"""
    assert triangle_number(1) is True, "1 is a special case Triangle Number"
    assert triangle_number(6) is True, "6 is a Triangle Number"
    assert triangle_number(28) is True, "28 is a Triangle Number"
    assert triangle_number(7) is False, "7 is not a Triangle Number"
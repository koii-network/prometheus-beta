import pytest
from src.triangular_number import calculate_triangular_number

def test_triangular_number_zero():
    """Test triangular number for 0."""
    assert calculate_triangular_number(0) == 0

def test_triangular_number_positive():
    """Test triangular numbers for several positive inputs."""
    test_cases = [
        (1, 1),    # 1
        (2, 3),    # 1 + 2
        (3, 6),    # 1 + 2 + 3
        (4, 10),   # 1 + 2 + 3 + 4
        (5, 15),   # 1 + 2 + 3 + 4 + 5
        (10, 55)   # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    ]
    
    for n, expected in test_cases:
        assert calculate_triangular_number(n) == expected

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_triangular_number(-1)

def test_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number([1])
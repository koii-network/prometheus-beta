import pytest
from src.triangular_number import calculate_triangular_number

def test_triangular_number_zero():
    assert calculate_triangular_number(0) == 0

def test_triangular_number_positive():
    # Check some known triangular numbers
    assert calculate_triangular_number(1) == 1   # 1
    assert calculate_triangular_number(2) == 3   # 1 + 2
    assert calculate_triangular_number(3) == 6   # 1 + 2 + 3
    assert calculate_triangular_number(4) == 10  # 1 + 2 + 3 + 4
    assert calculate_triangular_number(5) == 15  # 1 + 2 + 3 + 4 + 5

def test_triangular_number_large():
    assert calculate_triangular_number(100) == 5050

def test_triangular_number_negative_input():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_triangular_number(-1)

def test_triangular_number_invalid_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number("5")
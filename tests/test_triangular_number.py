import pytest
from src.triangular_number import calculate_triangular_number

def test_triangular_number_valid_inputs():
    # Test several known triangular numbers
    assert calculate_triangular_number(0) == 0
    assert calculate_triangular_number(1) == 1
    assert calculate_triangular_number(2) == 3
    assert calculate_triangular_number(3) == 6
    assert calculate_triangular_number(4) == 10
    assert calculate_triangular_number(5) == 15
    assert calculate_triangular_number(10) == 55

def test_triangular_number_large_input():
    # Test a larger input
    assert calculate_triangular_number(100) == 5050

def test_triangular_number_negative_input():
    # Test that negative inputs raise a ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_triangular_number(-1)

def test_triangular_number_invalid_type():
    # Test that non-integer inputs raise a TypeError
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        calculate_triangular_number("5")
import pytest
from src.triangle_number import triangle_number

def test_triangle_number_valid_triangle_numbers():
    """Test known Triangle Numbers."""
    valid_numbers = [6, 28, 496, 8128]
    for num in valid_numbers:
        assert triangle_number(num) == True, f"{num} should be a Triangle Number"

def test_triangle_number_invalid_numbers():
    """Test numbers that are not Triangle Numbers."""
    invalid_numbers = [12, 18, 20, 100, 1000]
    for num in invalid_numbers:
        assert triangle_number(num) == False, f"{num} should not be a Triangle Number"

def test_triangle_number_boundary_cases():
    """Test boundary and edge cases."""
    assert triangle_number(1) == False, "1 is not a Triangle Number"
    assert triangle_number(0) == False, "0 should return False"
    assert triangle_number(-5) == False, "Negative numbers should return False"

def test_triangle_number_type_validation():
    """Test input type validation."""
    with pytest.raises(TypeError):
        triangle_number(None)
    with pytest.raises(TypeError):
        triangle_number("not a number")
    with pytest.raises(TypeError):
        triangle_number([1, 2, 3])
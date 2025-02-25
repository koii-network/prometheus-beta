import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_rectangle_perimeter_valid_inputs():
    """Test perimeter calculation with valid numeric inputs."""
    assert calculate_rectangle_perimeter(5, 3) == 16
    assert calculate_rectangle_perimeter(10, 7) == 34
    assert calculate_rectangle_perimeter(0, 0) == 0
    assert calculate_rectangle_perimeter(2.5, 4.5) == 14.0

def test_rectangle_perimeter_integer_inputs():
    """Test perimeter calculation with integer inputs."""
    assert calculate_rectangle_perimeter(5, 5) == 20
    assert calculate_rectangle_perimeter(0, 10) == 20

def test_rectangle_perimeter_negative_inputs():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(-1, 5)
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(5, -3)
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(-2, -2)

def test_rectangle_perimeter_invalid_type():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter("5", 3)
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(5, "3")
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter([], {})
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(None, None)
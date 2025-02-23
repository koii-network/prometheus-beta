import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_standard_rectangle_perimeter():
    """Test perimeter calculation for a standard rectangle."""
    assert calculate_rectangle_perimeter(5, 3) == 16

def test_zero_dimensions():
    """Test perimeter calculation when one or both dimensions are zero."""
    assert calculate_rectangle_perimeter(0, 5) == 10
    assert calculate_rectangle_perimeter(5, 0) == 10
    assert calculate_rectangle_perimeter(0, 0) == 0

def test_float_dimensions():
    """Test perimeter calculation with float values."""
    assert calculate_rectangle_perimeter(2.5, 3.5) == 12.0

def test_negative_dimensions_raise_error():
    """Test that negative dimensions raise a ValueError."""
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(-1, 5)
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(5, -1)
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(-1, -1)

def test_invalid_type_inputs():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter("5", 3)
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(5, "3")
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(None, 3)
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(5, None)
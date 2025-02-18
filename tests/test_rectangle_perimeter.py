import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_rectangle_perimeter_positive_numbers():
    """Test perimeter calculation for positive numbers."""
    assert calculate_rectangle_perimeter(5, 3) == 16
    assert calculate_rectangle_perimeter(10, 7) == 34
    assert calculate_rectangle_perimeter(0, 0) == 0

def test_rectangle_perimeter_floating_point():
    """Test perimeter calculation for floating point numbers."""
    assert calculate_rectangle_perimeter(2.5, 3.5) == pytest.approx(12.0)
    assert calculate_rectangle_perimeter(1.1, 2.2) == pytest.approx(6.6)

def test_rectangle_perimeter_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers"):
        calculate_rectangle_perimeter(-1, 5)
    
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers"):
        calculate_rectangle_perimeter(5, -3)
    
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers"):
        calculate_rectangle_perimeter(-1, -1)
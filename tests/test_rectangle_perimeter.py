import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_rectangle_perimeter_positive_integers():
    assert calculate_rectangle_perimeter(5, 3) == 16

def test_rectangle_perimeter_floating_point():
    assert calculate_rectangle_perimeter(2.5, 4.5) == 14.0

def test_rectangle_perimeter_zero():
    assert calculate_rectangle_perimeter(0, 10) == 20

def test_rectangle_perimeter_negative_input():
    with pytest.raises(ValueError, match="Length and width must be non-negative values"):
        calculate_rectangle_perimeter(-1, 5)
    
    with pytest.raises(ValueError, match="Length and width must be non-negative values"):
        calculate_rectangle_perimeter(5, -3)
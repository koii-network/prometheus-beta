import pytest
from src.sum_of_squares import sum_of_squares

def test_sum_of_squares_normal_case():
    """Test sum of squares with regular integers"""
    assert sum_of_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_with_zero():
    """Test sum of squares including zero"""
    assert sum_of_squares([0, 1, 2]) == 5  # 0^2 + 1^2 + 2^2 = 0 + 1 + 4 = 5

def test_sum_of_squares_with_negative_numbers():
    """Test sum of squares with negative numbers"""
    assert sum_of_squares([-1, -2, 3]) == 14  # (-1)^2 + (-2)^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_with_floats():
    """Test sum of squares with floating point numbers"""
    assert sum_of_squares([1.5, 2.5]) == pytest.approx(8.5)  # 1.5^2 + 2.5^2 = 2.25 + 6.25 = 8.5

def test_sum_of_squares_empty_list():
    """Test sum of squares with an empty list"""
    assert sum_of_squares([]) == 0

def test_sum_of_squares_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares("not a list")

def test_sum_of_squares_invalid_list_elements():
    """Test that TypeError is raised for non-numeric list elements"""
    with pytest.raises(TypeError, match="All elements in the list must be numeric"):
        sum_of_squares([1, 2, "three"])
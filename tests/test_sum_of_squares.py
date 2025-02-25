import pytest
from src.sum_of_squares import sum_of_squares

def test_sum_of_squares_basic():
    """Test sum of squares with basic positive integers."""
    assert sum_of_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_empty_list():
    """Test sum of squares with an empty list."""
    assert sum_of_squares([]) == 0

def test_sum_of_squares_negative_numbers():
    """Test sum of squares with negative numbers."""
    assert sum_of_squares([-1, -2, -3]) == 14  # Same as positive numbers due to squaring

def test_sum_of_squares_mixed_numbers():
    """Test sum of squares with mixed positive and negative numbers."""
    assert sum_of_squares([-1, 2, -3]) == 14

def test_sum_of_squares_float_numbers():
    """Test sum of squares with float numbers."""
    assert sum_of_squares([1.5, 2.5]) == pytest.approx(8.5)  # 1.5^2 + 2.5^2 = 2.25 + 6.25 = 8.5

def test_sum_of_squares_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares(123)

def test_sum_of_squares_non_numeric_elements():
    """Test that a TypeError is raised for non-numeric list elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        sum_of_squares([1, 2, 'a'])
        sum_of_squares([1, 2, [3]])
        sum_of_squares([1, 2, None])
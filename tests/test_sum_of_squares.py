import pytest
from src.sum_of_squares import sum_of_squares

def test_sum_of_squares_positive_numbers():
    assert sum_of_squares([1, 2, 3]) == 14

def test_sum_of_squares_negative_numbers():
    assert sum_of_squares([-1, -2, -3]) == 14

def test_sum_of_squares_mixed_numbers():
    assert sum_of_squares([-1, 0, 1]) == 2

def test_sum_of_squares_floats():
    assert sum_of_squares([1.5, 2.5]) == round(1.5**2 + 2.5**2, 5)

def test_sum_of_squares_empty_list():
    assert sum_of_squares([]) == 0

def test_sum_of_squares_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares(123)

def test_sum_of_squares_invalid_input_non_numeric():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        sum_of_squares([1, 2, 'three'])
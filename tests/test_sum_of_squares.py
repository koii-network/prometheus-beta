import pytest
from src.sum_of_squares import sum_of_squares

def test_sum_of_squares_positive_numbers():
    assert sum_of_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_zero():
    assert sum_of_squares([0, 0, 0]) == 0

def test_sum_of_squares_negative_numbers():
    assert sum_of_squares([-1, -2, -3]) == 14  # Same as positive numbers due to squaring

def test_sum_of_squares_mixed_numbers():
    assert sum_of_squares([-1, 2, -3]) == 14

def test_sum_of_squares_empty_list():
    assert sum_of_squares([]) == 0

def test_sum_of_squares_float_numbers():
    assert sum_of_squares([1.5, 2.5]) == pytest.approx(8.5)  # 1.5^2 + 2.5^2 = 2.25 + 6.25 = 8.5

def test_sum_of_squares_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares("not a list")

def test_sum_of_squares_invalid_input_non_numeric():
    with pytest.raises(TypeError, match="All elements in the list must be numeric"):
        sum_of_squares([1, 2, "three"])
import pytest
from src.integer_list_sum import sum_integers

def test_sum_integers_positive_numbers():
    assert sum_integers([1, 2, 3, 4, 5]) == 15

def test_sum_integers_negative_numbers():
    assert sum_integers([-1, -2, -3, -4, -5]) == -15

def test_sum_integers_mixed_numbers():
    assert sum_integers([-10, 0, 10, 20]) == 20

def test_sum_integers_empty_list():
    assert sum_integers([]) == 0

def test_sum_integers_single_element():
    assert sum_integers([42]) == 42

def test_sum_integers_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(123)

def test_sum_integers_non_integer_elements():
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, "3", 4, 5])
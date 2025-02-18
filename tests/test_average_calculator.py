import pytest
from src.average_calculator import calculate_average

def test_calculate_average_normal_list():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([-1, 0, 1]) == 0

def test_calculate_average_floating_point():
    assert round(calculate_average([1.5, 2.5, 3.5]), 2) == 2.5

def test_calculate_average_single_element():
    assert calculate_average([42]) == 42

def test_calculate_average_empty_list():
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_calculate_average_non_numeric():
    with pytest.raises(TypeError, match="All elements in the list must be numeric"):
        calculate_average([1, 2, '3', 4])
        calculate_average([1, 2, None, 4])
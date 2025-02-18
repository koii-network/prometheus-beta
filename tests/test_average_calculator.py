import pytest
from src.average_calculator import calculate_average

def test_calculate_average_normal_list():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([0, 0, 0]) == 0.0
    assert calculate_average([-1, 1]) == 0.0

def test_calculate_average_floating_point():
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_empty_list():
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_calculate_average_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average(123)

def test_calculate_average_non_numeric_list():
    with pytest.raises(TypeError, match="List must contain only numeric values"):
        calculate_average([1, 2, '3'])
    with pytest.raises(TypeError, match="List must contain only numeric values"):
        calculate_average([1, 2, None])
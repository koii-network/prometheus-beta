import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_scalar():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    expected = [[2, 4], [6, 8]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_multiply_array():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': [[2, 3], [4, 5]]}
    expected = [[2, 6], [12, 20]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_add_scalar():
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': 2}
    expected = [[3, 4], [5, 6]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_add_array():
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': [[2, 3], [4, 5]]}
    expected = [[3, 5], [7, 9]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_transpose():
    arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': True}
    expected = [[1, 3], [2, 4]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_multiple_manipulations():
    arr = [[1, 2], [3, 4]]
    manipulations = {
        'multiply': 2,
        'add': 1,
        'transpose': True
    }
    expected = [[3, 7], [5, 9]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_error_invalid_manipulation():
    arr = [[1, 2], [3, 4]]
    manipulations = {'invalid_op': True}
    with pytest.raises(ValueError, match="Unsupported manipulation"):
        multiArrayManipulator(arr, manipulations)

def test_error_multiply_dimension_mismatch():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': [[1, 2, 3], [4, 5, 6]]}
    with pytest.raises(ValueError, match="Multiplication array must match input array dimensions"):
        multiArrayManipulator(arr, manipulations)

def test_error_add_dimension_mismatch():
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': [[1, 2, 3], [4, 5, 6]]}
    with pytest.raises(ValueError, match="Addition array must match input array dimensions"):
        multiArrayManipulator(arr, manipulations)

def test_error_empty_array():
    arr = []
    manipulations = {'multiply': 2}
    with pytest.raises(ValueError, match="Input must be a non-empty 2D list"):
        multiArrayManipulator(arr, manipulations)

def test_error_non_2d_array():
    arr = [1, 2, 3]
    manipulations = {'multiply': 2}
    with pytest.raises(ValueError, match="Input must be a non-empty 2D list"):
        multiArrayManipulator(arr, manipulations)
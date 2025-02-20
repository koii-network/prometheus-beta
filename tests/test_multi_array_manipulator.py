import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    expected = [[2, 4], [6, 8]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_add_operation():
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'add': 10}
    expected = [[11, 12], [13, 14]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_transpose_operation():
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': True}
    expected = [[1, 3], [2, 4]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_multiple_operations():
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2, 'add': 10, 'transpose': True}
    expected = [[12, 16], [14, 18]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_no_operations():
    input_arr = [[1, 2], [3, 4]]
    manipulations = {}
    expected = [[1, 2], [3, 4]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_empty_array():
    input_arr = []
    manipulations = {'multiply': 2}
    expected = []
    assert multiArrayManipulator(input_arr, manipulations) == expected
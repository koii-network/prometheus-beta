import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    # Test multiply operation
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    expected = [[2, 4], [6, 8]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_add_operation():
    # Test add operation
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'add': 5}
    expected = [[6, 7], [8, 9]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_transpose_operation():
    # Test transpose operation
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': True}
    expected = [[1, 3], [2, 4]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_combined_operations():
    # Test multiple operations together
    input_arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2, 'add': 3, 'transpose': True}
    expected = [[5, 7], [6, 9]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_no_operations():
    # Test when no operations are specified
    input_arr = [[1, 2], [3, 4]]
    manipulations = {}
    expected = [[1, 2], [3, 4]]
    assert multiArrayManipulator(input_arr, manipulations) == expected

def test_empty_array():
    # Test with an empty array
    input_arr = []
    manipulations = {'multiply': 2}
    expected = []
    assert multiArrayManipulator(input_arr, manipulations) == expected
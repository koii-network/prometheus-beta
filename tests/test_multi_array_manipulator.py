import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from multi_array_manipulator import multiArrayManipulator

def test_scalar_multiply():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    result = multiArrayManipulator(arr, manipulations)
    assert result == [[2, 4], [6, 8]]

def test_scalar_add():
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': 5}
    result = multiArrayManipulator(arr, manipulations)
    assert result == [[6, 7], [8, 9]]

def test_matrix_multiply():
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': [[2, 0], [0, 2]]}
    result = multiArrayManipulator(arr, manipulations)
    assert result == [[2, 4], [6, 8]]

def test_matrix_add():
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': [[1, 1], [1, 1]]}
    result = multiArrayManipulator(arr, manipulations)
    assert result == [[2, 3], [4, 5]]

def test_transpose():
    arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': None}
    result = multiArrayManipulator(arr, manipulations)
    assert result == [[1, 3], [2, 4]]

def test_multiple_operations():
    arr = [[1, 2], [3, 4]]
    manipulations = {
        'multiply': 2,
        'add': 1,
        'transpose': None
    }
    result = multiArrayManipulator(arr, manipulations)
    assert result == [[3, 7], [5, 9]]

def test_empty_array():
    arr = []
    manipulations = {'multiply': 2}
    result = multiArrayManipulator(arr, manipulations)
    assert result == []
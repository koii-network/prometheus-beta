import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    # Test multiplying each element by a factor
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    expected = [[2, 4], [6, 8]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_add_operation():
    # Test adding a value to each element
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': 10}
    expected = [[11, 12], [13, 14]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_transpose_operation():
    # Test transposing a 2D array
    arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': True}
    expected = [[1, 3], [2, 4]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_multiple_operations():
    # Test multiple operations in sequence
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2, 'add': 5, 'transpose': True}
    expected = [[7, 11], [8, 12]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_no_manipulations():
    # Test when no manipulations are provided
    arr = [[1, 2], [3, 4]]
    manipulations = {}
    assert multiArrayManipulator(arr, manipulations) == arr

def test_empty_array():
    # Test with an empty array
    arr = []
    manipulations = {'multiply': 2}
    assert multiArrayManipulator(arr, manipulations) == []

def test_does_not_modify_original():
    # Ensure the original array is not modified
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    multiArrayManipulator(arr, manipulations)
    assert arr == [[1, 2], [3, 4]]
import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    """Test multiplication operation."""
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    expected = [[2, 4], [6, 8]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_add_operation():
    """Test addition operation."""
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': 3}
    expected = [[4, 5], [6, 7]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_transpose_operation():
    """Test transpose operation."""
    arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': None}
    expected = [[1, 3], [2, 4]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_multiple_operations():
    """Test multiple operations in sequence."""
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2, 'add': 1, 'transpose': None}
    expected = [[3, 7], [5, 9]]
    assert multiArrayManipulator(arr, manipulations) == expected

def test_empty_array_error():
    """Test error handling for empty array."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        multiArrayManipulator([], {})

def test_invalid_input_type():
    """Test error handling for invalid input type."""
    with pytest.raises(TypeError, match="Input must be a 2D list of integers"):
        multiArrayManipulator("not a list", {})

def test_invalid_manipulation():
    """Test error handling for unsupported manipulation."""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Unsupported manipulation"):
        multiArrayManipulator(arr, {'invalid_op': 1})

def test_invalid_multiply_type():
    """Test error handling for invalid multiply type."""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(TypeError, match="Multiply value must be a number"):
        multiArrayManipulator(arr, {'multiply': 'not a number'})

def test_invalid_add_type():
    """Test error handling for invalid add type."""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(TypeError, match="Add value must be a number"):
        multiArrayManipulator(arr, {'add': 'not a number'})

def test_non_square_array_transpose():
    """Test transpose on a non-square array."""
    arr = [[1, 2, 3], [4, 5, 6]]
    manipulations = {'transpose': None}
    expected = [[1, 4], [2, 5], [3, 6]]
    assert multiArrayManipulator(arr, manipulations) == expected
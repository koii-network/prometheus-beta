import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from matrix_addition import add_matrices

def test_basic_matrix_addition():
    """Test basic matrix addition with integer matrices"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_matrix_addition_with_floats():
    """Test matrix addition with floating point numbers"""
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    expected = [[2.0, 4.0], [6.0, 8.0]]
    assert add_matrices(matrix1, matrix2) == expected

def test_matrix_different_dimensions_raises_error():
    """Test that adding matrices of different dimensions raises an error"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same dimensions"):
        add_matrices(matrix1, matrix2)

def test_empty_matrix_raises_error():
    """Test that empty matrices raise an error"""
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [[1, 2]])
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([[1, 2]], [])

def test_non_rectangular_matrix_raises_error():
    """Test that non-rectangular matrices raise an error"""
    matrix1 = [[1, 2], [3]]
    matrix2 = [[4, 5], [6, 7]]
    with pytest.raises(ValueError, match="All rows in matrix1 must have the same length"):
        add_matrices(matrix1, matrix2)

def test_non_numeric_matrix_raises_error():
    """Test that matrices with non-numeric elements raise an error"""
    matrix1 = [[1, 2], [3, 'a']]
    matrix2 = [[4, 5], [6, 7]]
    with pytest.raises(TypeError, match="Matrix elements must be numeric"):
        add_matrices(matrix1, matrix2)

def test_non_list_input_raises_error():
    """Test that non-list inputs raise an error"""
    with pytest.raises(TypeError, match="Inputs must be lists of lists"):
        add_matrices(1, [[1, 2]])
    with pytest.raises(TypeError, match="Inputs must be lists of lists"):
        add_matrices([[1, 2]], "not a list")

def test_single_element_matrix():
    """Test matrix addition with single-element matrices"""
    matrix1 = [[5]]
    matrix2 = [[3]]
    expected = [[8]]
    assert add_matrices(matrix1, matrix2) == expected
"""
Test suite for matrix operations module.
"""
import pytest
from src.matrix_operations import add_matrices


def test_basic_matrix_addition():
    """Test basic matrix addition with integer matrices."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected


def test_matrix_addition_with_floats():
    """Test matrix addition with floating-point numbers."""
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    expected = [[2.0, 4.0], [6.0, 8.0]]
    assert add_matrices(matrix1, matrix2) == expected


def test_incompatible_matrix_dimensions():
    """Test that an error is raised when matrices have different dimensions."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same dimensions"):
        add_matrices(matrix1, matrix2)


def test_empty_matrix_error():
    """Test that an error is raised for empty matrices."""
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [[1, 2]])
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([[1, 2]], [])


def test_non_rectangular_matrix():
    """Test that an error is raised for non-rectangular matrices."""
    matrix1 = [[1, 2], [3]]
    matrix2 = [[4, 5], [6, 7]]
    with pytest.raises(ValueError, match="Rows in first matrix must have equal length"):
        add_matrices(matrix1, matrix2)


def test_non_numeric_matrix():
    """Test that an error is raised for non-numeric matrix elements."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 'a'], [3, 4]]
    with pytest.raises(TypeError, match="Matrix elements must be numeric"):
        add_matrices(matrix1, matrix2)


def test_non_list_input():
    """Test that an error is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        add_matrices("not a list", [[1, 2]])
    with pytest.raises(TypeError, match="Inputs must be lists"):
        add_matrices([[1, 2]], "not a list")
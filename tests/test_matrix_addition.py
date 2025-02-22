import pytest
from src.matrix_addition import add_matrices

def test_basic_matrix_addition():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_different_matrix_sizes_raises_error():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same number of columns in each row"):
        add_matrices(matrix1, matrix2)

def test_different_row_counts_raises_error():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 2]]
    with pytest.raises(ValueError, match="Matrices must have the same number of rows"):
        add_matrices(matrix1, matrix2)

def test_empty_matrices_raises_error():
    matrix1 = []
    matrix2 = [[1, 2]]
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices(matrix1, matrix2)

def test_single_element_matrices():
    matrix1 = [[5]]
    matrix2 = [[3]]
    expected = [[8]]
    assert add_matrices(matrix1, matrix2) == expected

def test_rectangular_matrices():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8, 9], [10, 11, 12]]
    expected = [[8, 10, 12], [14, 16, 18]]
    assert add_matrices(matrix1, matrix2) == expected
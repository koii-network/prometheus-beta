import pytest
from src.sparse_matrix_mult import sparse_matrix_multiply

def test_basic_sparse_matrix_multiplication():
    # Simple multiplication of 2x2 matrices
    matrix1 = {
        0: {0: 1, 1: 2},
        1: {0: 3, 1: 4}
    }
    matrix2 = {
        0: {0: 5, 1: 6},
        1: {0: 7, 1: 8}
    }
    expected = {
        0: {0: 19, 1: 22},
        1: {0: 43, 1: 50}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_sparse_matrix_with_zeros():
    # Matrix with some zero entries
    matrix1 = {
        0: {0: 1, 2: 3},
        1: {1: 2}
    }
    matrix2 = {
        0: {0: 4, 1: 5},
        1: {0: 6},
        2: {1: 7}
    }
    expected = {
        0: {0: 4, 1: 15},
        1: {1: 14}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_empty_matrix_multiplication():
    # Empty matrix multiplication
    assert sparse_matrix_multiply({}, {}) == {}
    assert sparse_matrix_multiply({0: {}}, {}) == {}
    assert sparse_matrix_multiply({}, {0: {}}) == {}

def test_matrix_with_single_non_zero_entry():
    # Matrix with a single non-zero entry
    matrix1 = {0: {0: 5}}
    matrix2 = {0: {1: 3}}
    expected = {0: {1: 15}}
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_different_sized_matrices():
    # Matrices with different numbers of rows and columns
    matrix1 = {
        0: {0: 1, 1: 2, 2: 3},
        1: {0: 4, 1: 5, 2: 6}
    }
    matrix2 = {
        0: {0: 7, 1: 8},
        1: {0: 9, 1: 10},
        2: {0: 11, 1: 12}
    }
    expected = {
        0: {0: 58, 1: 64},
        1: {0: 139, 1: 154}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_sparse_matrices_with_some_zero_rows():
    # Matrices with some completely zero rows
    matrix1 = {
        0: {0: 1, 1: 2},
        1: {},  # Zero row
        2: {0: 3, 1: 4}
    }
    matrix2 = {
        0: {0: 5, 1: 6},
        1: {0: 7, 1: 8},
        2: {0: 9, 1: 10}
    }
    expected = {
        0: {0: 19, 1: 22},
        2: {0: 51, 1: 58}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected
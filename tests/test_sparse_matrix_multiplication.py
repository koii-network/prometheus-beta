import pytest
from src.sparse_matrix_multiplication import sparse_matrix_multiply

def test_basic_multiplication():
    # Basic multiplication of 2x2 sparse matrices
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

def test_rectangular_matrices():
    # Rectangular sparse matrices
    matrix1 = {
        0: {0: 1, 1: 2},
        1: {0: 3, 1: 4}
    }
    matrix2 = {
        0: {0: 5, 1: 6, 2: 7},
        1: {0: 8, 1: 9, 2: 10}
    }
    expected = {
        0: {0: 21, 1: 24, 2: 27},
        1: {0: 47, 1: 54, 2: 61}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_sparse_with_zeros():
    # Sparse matrices with many zero elements
    matrix1 = {
        0: {1: 2},
        2: {0: 3}
    }
    matrix2 = {
        0: {1: 5},
        1: {0: 7}
    }
    expected = {
        0: {0: 14},
        2: {1: 15}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_empty_matrices():
    # Empty matrix multiplication
    assert sparse_matrix_multiply({}, {}) == {}
    assert sparse_matrix_multiply({0: {}}, {0: {}}) == {}

def test_incompatible_dimensions():
    # Incompatible matrix dimensions
    matrix1 = {0: {0: 1}}
    matrix2 = {1: {0: 2}, 2: {0: 3}}
    with pytest.raises(ValueError, match="Matrix dimensions are incompatible for multiplication"):
        sparse_matrix_multiply(matrix1, matrix2)

def test_large_sparse_matrix():
    # Large sparse matrix with scattered non-zero elements
    matrix1 = {
        0: {100: 1},
        500: {200: 2}
    }
    matrix2 = {
        100: {300: 3},
        200: {400: 4}
    }
    expected = {
        0: {300: 3},
        500: {400: 8}
    }
    assert sparse_matrix_multiply(matrix1, matrix2) == expected
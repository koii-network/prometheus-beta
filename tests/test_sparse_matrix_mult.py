import pytest
from src.sparse_matrix_mult import sparse_matrix_multiply

def test_basic_sparse_matrix_multiplication():
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
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected

def test_empty_matrices():
    # Test multiplication with empty matrices
    assert sparse_matrix_multiply({}, {}) == {}
    assert sparse_matrix_multiply({0: {}}, {0: {}}) == {}

def test_sparse_matrix_with_zero_values():
    # Matrix with some zero values
    matrix1 = {
        0: {0: 1, 1: 0},
        1: {0: 3, 1: 0}
    }
    matrix2 = {
        0: {0: 0, 1: 6},
        1: {0: 7, 1: 8}
    }
    
    expected = {
        1: {1: 0}
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == {}

def test_different_size_sparse_matrices():
    # Matrices with different structures
    matrix1 = {
        0: {1: 2},
        2: {0: 3}
    }
    matrix2 = {
        1: {1: 5},
        0: {0: 7}
    }
    
    expected = {
        0: {0: 14},
        2: {1: 15}
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected

def test_multiplication_with_incompatible_dimensions():
    # Matrices that can't be multiplied
    matrix1 = {
        0: {0: 1, 2: 2},
        1: {1: 3}
    }
    matrix2 = {
        0: {1: 4},
        2: {2: 5}
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == {}
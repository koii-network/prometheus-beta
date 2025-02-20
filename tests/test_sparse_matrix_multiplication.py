import pytest
from src.sparse_matrix_multiplication import sparse_matrix_multiply

def test_basic_multiplication():
    # Basic multiplication of two sparse matrices
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
    matrix1 = {}
    matrix2 = {}
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == {}

def test_sparse_matrix_with_zeros():
    # Test multiplication with sparse matrices containing zero values
    matrix1 = {
        0: {0: 1, 2: 3},
        1: {1: 2}
    }
    matrix2 = {
        0: {0: 4, 1: 0},
        1: {0: 0, 1: 5},
        2: {0: 6, 1: 7}
    }
    
    expected = {
        0: {0: 4, 1: 15},
        1: {1: 10}
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected

def test_incompatible_matrix_dimensions():
    # Test raising ValueError for incompatible matrix dimensions
    matrix1 = {
        0: {0: 1, 1: 2, 2: 3},
        1: {0: 4, 1: 5, 2: 6}
    }
    matrix2 = {
        0: {0: 7, 1: 8},
        1: {0: 9, 1: 10}
    }
    
    with pytest.raises(ValueError, match="Matrix dimensions incompatible"):
        sparse_matrix_multiply(matrix1, matrix2)

def test_single_element_matrices():
    # Test multiplication with single-element matrices
    matrix1 = {0: {0: 2}}
    matrix2 = {0: {0: 3}}
    
    expected = {0: {0: 6}}
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected
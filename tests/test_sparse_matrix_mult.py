import pytest
from src.sparse_matrix_mult import sparse_matrix_multiply

def test_basic_sparse_matrix_multiplication():
    # Basic multiplication of 2x2 sparse matrices
    matrix1 = {
        0: {0: 1, 1: 2},  # First row
        1: {0: 3, 1: 4}   # Second row
    }
    matrix2 = {
        0: {0: 5, 1: 6},  # First row
        1: {0: 7, 1: 8}   # Second row
    }
    
    expected = {
        0: {0: 19, 1: 22},  # (1*5 + 2*7, 1*6 + 2*8)
        1: {0: 43, 1: 50}   # (3*5 + 4*7, 3*6 + 4*8)
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected

def test_sparse_matrix_with_different_dimensions():
    # Rectangular sparse matrices
    matrix1 = {
        0: {0: 1, 1: 2},
        1: {0: 3, 1: 4}
    }
    matrix2 = {
        0: {2: 5},
        1: {2: 6}
    }
    
    expected = {
        0: {2: 17},  # 1*5 + 2*6
        1: {2: 39}   # 3*5 + 4*6
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected

def test_sparse_matrix_with_zero_values():
    # Matrices with zero values
    matrix1 = {
        0: {0: 0, 1: 2},
        1: {0: 3, 1: 0}
    }
    matrix2 = {
        0: {0: 5, 1: 0},
        1: {0: 0, 1: 8}
    }
    
    expected = {
        0: {1: 16},  # 2*8
        1: {0: 15}   # 3*5
    }
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == expected

def test_empty_matrix_multiplication():
    # Empty matrices
    matrix1 = {}
    matrix2 = {}
    
    result = sparse_matrix_multiply(matrix1, matrix2)
    assert result == {}

def test_invalid_input_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        sparse_matrix_multiply([1, 2, 3], {})
    
    with pytest.raises(TypeError):
        sparse_matrix_multiply({}, [1, 2, 3])
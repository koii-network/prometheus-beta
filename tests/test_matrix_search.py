import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    # Test existing values
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False
    assert search_matrix(matrix, 34) == True

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    
    # Single row matrix
    single_row_matrix = [[1, 3, 5]]
    assert search_matrix(single_row_matrix, 3) == True
    assert search_matrix(single_row_matrix, 4) == False
    
    # Single column matrix
    single_col_matrix = [[1], [3], [5]]
    assert search_matrix(single_col_matrix, 3) == True
    assert search_matrix(single_col_matrix, 4) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    # Test first and last values
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True
    
    # Test values just outside the matrix
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 61) == False
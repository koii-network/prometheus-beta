import pytest
from src.matrix_search import search_matrix

def test_search_matrix_normal_case():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    # Test existing values
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False
    assert search_matrix(matrix, 60) == True
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 23) == True

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    
    # Single row matrix
    matrix_single_row = [[1, 3, 5]]
    assert search_matrix(matrix_single_row, 3) == True
    assert search_matrix(matrix_single_row, 4) == False
    
    # Single column matrix
    matrix_single_col = [[1], [3], [5]]
    assert search_matrix(matrix_single_col, 3) == True
    assert search_matrix(matrix_single_col, 4) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    # Test minimum and maximum values
    assert search_matrix(matrix, 1) == True  # First value
    assert search_matrix(matrix, 60) == True  # Last value
    
    # Test values outside the range
    assert search_matrix(matrix, 0) == False  # Below minimum
    assert search_matrix(matrix, 61) == False  # Above maximum

def test_search_matrix_large_matrix():
    # Create a larger matrix to test scalability
    matrix = [[i * 10 + j for j in range(10)] for i in range(10)]
    
    for i in range(10):
        for j in range(10):
            assert search_matrix(matrix, i * 10 + j) == True
    
    # Test some values not in the matrix
    assert search_matrix(matrix, 100) == False
    assert search_matrix(matrix, -1) == False
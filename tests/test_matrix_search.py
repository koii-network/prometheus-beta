import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    
    # Basic search
    assert search_matrix(matrix, 9) == (1, 1)
    assert search_matrix(matrix, 17) == (2, 2)
    assert search_matrix(matrix, 1) == (0, 0)
    
    # Not found cases
    assert search_matrix(matrix, 0) == (-1, -1)
    assert search_matrix(matrix, 18) == (-1, -1)

def test_search_matrix_constraints():
    matrix = [
        [1, 3, 5, 7],
        [8, 10, 12, 14],
        [15, 17, 19, 21],
        [22, 24, 26, 28]
    ]
    
    # Test row range constraint
    assert search_matrix(matrix, 10, {'row_range': (1, 2)}) == (1, 1)
    assert search_matrix(matrix, 1, {'row_range': (1, 4)}) == (-1, -1)
    
    # Test column range constraint
    assert search_matrix(matrix, 12, {'col_range': (2, 3)}) == (1, 2)
    assert search_matrix(matrix, 12, {'col_range': (0, 2)}) == (-1, -1)

def test_search_matrix_sorted_constraints():
    matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17]
    ]
    
    # Test sorting constraints with sorted matrix
    constraints = {
        'sorted_rows': True,
        'sorted_cols': True
    }
    
    assert search_matrix(matrix, 6, constraints) == (2, 1)
    assert search_matrix(matrix, 16, constraints) == (2, 3)
    assert search_matrix(matrix, 13, constraints) == (3, 1)
    assert search_matrix(matrix, 20, constraints) == (-1, -1)

def test_matrix_search_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == (-1, -1)
    assert search_matrix([[]], 5) == (-1, -1)
    
    # Invalid constraints
    matrix = [[1, 2], [3, 4]]
    assert search_matrix(matrix, 2, {'row_range': (5, 10)}) == (-1, -1)
    assert search_matrix(matrix, 2, {'col_range': (5, 10)}) == (-1, -1)
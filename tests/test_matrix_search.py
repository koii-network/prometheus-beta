import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 6) == False

def test_matrix_search_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[], []], 5) == False
    
    # Single element matrix
    assert search_matrix([[5]], 5) == True
    assert search_matrix([[5]], 6) == False

def test_matrix_search_boundary_values():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # Test first and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 9) == True
    
    # Test out-of-range values
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 10) == False
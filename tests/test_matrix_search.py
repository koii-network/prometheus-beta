import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_matrix_search_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[]], 5) == False
    
    # Single element matrix
    assert search_matrix([[1]], 1) == True
    assert search_matrix([[1]], 2) == False

def test_matrix_search_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # First and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True
    
    # Values just outside the range
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 61) == False

def test_matrix_search_large_range():
    matrix = [
        [1, 100, 1000, 10000],
        [20000, 30000, 40000, 50000],
        [60000, 70000, 80000, 90000]
    ]
    assert search_matrix(matrix, 100) == True
    assert search_matrix(matrix, 35000) == False
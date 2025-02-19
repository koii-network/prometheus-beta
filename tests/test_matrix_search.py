import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[]], 5) == False

    # Single element matrix
    assert search_matrix([[1]], 1) == True
    assert search_matrix([[1]], 2) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # First and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True

def test_search_matrix_large_matrix():
    matrix = [[j * 10 + i for i in range(10)] for j in range(10)]
    # Test various values
    assert search_matrix(matrix, 42) == True
    assert search_matrix(matrix, 100) == False
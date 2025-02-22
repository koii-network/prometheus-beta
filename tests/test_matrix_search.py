import pytest
from src.matrix_search import search_matrix

def test_matrix_search_existing_target():
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
    
    # Single row matrix
    single_row_matrix = [[1, 3, 5]]
    assert search_matrix(single_row_matrix, 3) == True
    assert search_matrix(single_row_matrix, 4) == False
    
    # Single column matrix
    single_col_matrix = [[1], [3], [5]]
    assert search_matrix(single_col_matrix, 3) == True
    assert search_matrix(single_col_matrix, 4) == False

def test_matrix_search_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 1) == True  # First element
    assert search_matrix(matrix, 60) == True  # Last element
    assert search_matrix(matrix, 0) == False  # Below first element
    assert search_matrix(matrix, 61) == False  # Above last element

def test_matrix_search_large_matrix():
    large_matrix = [[x for x in range(i*10, (i+1)*10)] for i in range(100)]
    assert search_matrix(large_matrix, 42) == True
    assert search_matrix(large_matrix, 1000) == False
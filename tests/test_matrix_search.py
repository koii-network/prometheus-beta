import pytest
from src.matrix_search import search_matrix

def test_matrix_search_standard_case():
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
    
    # Empty row
    matrix_with_empty_row = [[], [1, 2, 3]]
    assert search_matrix(matrix_with_empty_row, 2) == True
    assert search_matrix(matrix_with_empty_row, 4) == False

def test_matrix_search_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # First and last elements
    assert search_matrix(matrix, 1) == True   # First element of first row
    assert search_matrix(matrix, 60) == True  # Last element of last row
    
    # Just outside boundary
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 61) == False

def test_matrix_search_unsorted_rows():
    matrix = [
        [10, 20, 30, 40],
        [1, 2, 3, 4],
        [50, 60, 70, 80]
    ]
    assert search_matrix(matrix, 2) == True
    assert search_matrix(matrix, 15) == False

def test_matrix_search_single_row_matrix():
    matrix = [[1, 3, 5]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 4) == False

def test_matrix_search_single_column_matrix():
    matrix = [[1], [3], [5]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 4) == False
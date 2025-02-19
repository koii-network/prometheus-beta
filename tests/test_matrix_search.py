import pytest
from src.matrix_search import search_sorted_matrix

def test_search_sorted_matrix_basic():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 13) == False

def test_search_sorted_matrix_edge_cases():
    # Empty matrix
    assert search_sorted_matrix([], 5) == False
    
    # Matrix with empty rows
    matrix = [[], [1, 2], []]
    assert search_sorted_matrix(matrix, 1) == True
    assert search_sorted_matrix(matrix, 3) == False

def test_search_sorted_matrix_single_row():
    matrix = [[1, 3, 5, 7]]
    assert search_sorted_matrix(matrix, 1) == True
    assert search_sorted_matrix(matrix, 7) == True
    assert search_sorted_matrix(matrix, 4) == False

def test_search_sorted_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_sorted_matrix(matrix, 1) == True   # First element
    assert search_sorted_matrix(matrix, 50) == True  # Last element
    assert search_sorted_matrix(matrix, 0) == False  # Below first element
    assert search_sorted_matrix(matrix, 51) == False  # Above last element

def test_search_sorted_matrix_unsorted_rows():
    matrix = [
        [10, 20, 30, 40],
        [1, 3, 5, 7],
        [15, 25, 35, 45]
    ]
    assert search_sorted_matrix(matrix, 5) == True
    assert search_sorted_matrix(matrix, 15) == True
    assert search_sorted_matrix(matrix, 8) == False
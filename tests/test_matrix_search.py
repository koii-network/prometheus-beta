import pytest
from src.matrix_search import search_sorted_matrix

def test_search_sorted_matrix_found():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 16) == True
    assert search_sorted_matrix(matrix, 50) == True

def test_search_sorted_matrix_not_found():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_sorted_matrix(matrix, 8) == False
    assert search_sorted_matrix(matrix, 21) == False
    assert search_sorted_matrix(matrix, 51) == False

def test_search_sorted_matrix_edge_cases():
    # Empty matrix
    assert search_sorted_matrix([], 5) == False
    
    # Matrix with empty rows
    assert search_sorted_matrix([[], []], 5) == False
    
    # Single row matrix
    matrix = [[1, 2, 3]]
    assert search_sorted_matrix(matrix, 2) == True
    assert search_sorted_matrix(matrix, 4) == False

def test_search_sorted_matrix_negative_numbers():
    matrix = [
        [-5, -3, 0, 2],
        [10, 12, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_sorted_matrix(matrix, -3) == True
    assert search_sorted_matrix(matrix, -4) == False
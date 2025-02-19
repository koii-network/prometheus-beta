import pytest
from src.matrix_search import search_matrix

def test_matrix_search_target_exists():
    # Matrix with unique integers, target in the matrix
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 16) == True
    assert search_matrix(matrix, 60) == True

def test_matrix_search_target_not_exists():
    # Matrix with unique integers, target not in the matrix
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 13) == False
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 100) == False

def test_matrix_search_single_element_matrix():
    # Single element matrix
    matrix = [[5]]
    assert search_matrix(matrix, 5) == True
    assert search_matrix(matrix, 6) == False

def test_matrix_search_empty_matrix_raises_error():
    # Empty matrix should raise ValueError
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix([[]], 5)

def test_matrix_search_edge_cases():
    # Matrices with different dimensions and edge values
    matrix1 = [[1, 3], [4, 5]]
    assert search_matrix(matrix1, 1) == True
    assert search_matrix(matrix1, 5) == True
    
    matrix2 = [[1]]
    assert search_matrix(matrix2, 1) == True
    assert search_matrix(matrix2, 2) == False
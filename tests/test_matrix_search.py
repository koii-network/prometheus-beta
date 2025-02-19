import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    # Basic successful search
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 17) == True

def test_matrix_search_not_found():
    # Search for elements not in matrix
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 10) == False
    assert search_matrix(matrix, 18) == False

def test_matrix_search_edge_cases():
    # Single row matrix
    matrix1 = [[1, 2, 3]]
    assert search_matrix(matrix1, 2) == True
    assert search_matrix(matrix1, 4) == False

    # Single column matrix
    matrix2 = [[1], [2], [3]]
    assert search_matrix(matrix2, 2) == True
    assert search_matrix(matrix2, 4) == False

def test_matrix_search_empty_matrix_raises_error():
    # Empty matrix should raise ValueError
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix([[]], 5)

def test_matrix_search_irregular_matrix_raises_error():
    # Irregular matrix should raise ValueError
    with pytest.raises(ValueError):
        search_matrix([[1, 2], [3]], 5)
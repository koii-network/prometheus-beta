import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic_found():
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
    
    # Matrix with single row
    matrix_single_row = [[1, 3, 5]]
    assert search_matrix(matrix_single_row, 3) == True
    assert search_matrix(matrix_single_row, 4) == False
    
    # Matrix with single column
    matrix_single_col = [[1], [3], [5]]
    assert search_matrix(matrix_single_col, 3) == True
    assert search_matrix(matrix_single_col, 4) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # First and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True
    
    # Boundary values not in matrix
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 61) == False

def test_search_matrix_invalid_inputs():
    # Non-list matrix
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_matrix("not a matrix", 5)
    
    # Matrix with non-list rows
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_matrix([1, 2, 3], 5)
    
    # Matrix with non-integer elements
    with pytest.raises(ValueError, match="Matrix must contain only integers"):
        search_matrix([[1, 2], [3, 'a']], 5)
    
    # Non-integer target
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_matrix([[1, 2], [3, 4]], "5")

def test_search_matrix_large_matrix():
    # Large matrix to test performance and edge cases
    large_matrix = [[i * 10 + j for j in range(10)] for i in range(100)]
    
    # Test finding a value
    assert search_matrix(large_matrix, 456) == True
    
    # Test value not in matrix
    assert search_matrix(large_matrix, 1001) == False
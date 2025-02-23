import pytest
from src.matrix_search import search_matrix

def test_search_matrix_target_present():
    """Test finding a target that exists in the matrix"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    """Test edge cases like first and last elements"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 1) == True  # First element
    assert search_matrix(matrix, 60) == True  # Last element
    assert search_matrix(matrix, 0) == False  # Less than first
    assert search_matrix(matrix, 61) == False  # Greater than last

def test_matrix_single_row():
    """Test matrix with a single row"""
    matrix = [[1, 3, 5, 7]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 4) == False

def test_matrix_single_column():
    """Test matrix with a single column"""
    matrix = [[1], [3], [5], [7]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 4) == False

def test_matrix_empty_input():
    """Test handling of empty matrix inputs"""
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix([[]], 5)

def test_search_matrix_large_input():
    """Test matrix search with a larger input"""
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_matrix(matrix, 5) == True
    assert search_matrix(matrix, 20) == False
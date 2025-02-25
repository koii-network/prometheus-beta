import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == (0, 1)
    assert search_matrix(matrix, 13) is None
    assert search_matrix(matrix, 34) == (2, 2)

def test_search_matrix_single_row():
    """Test matrix with a single row"""
    matrix = [[1, 3, 5]]
    assert search_matrix(matrix, 3) == (0, 1)
    assert search_matrix(matrix, 4) is None

def test_search_matrix_single_column():
    """Test matrix with a single column"""
    matrix = [[1], [3], [5]]
    assert search_matrix(matrix, 3) == (1, 0)
    assert search_matrix(matrix, 4) is None

def test_search_matrix_edge_cases():
    """Test edge cases"""
    # First and last elements
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 1) == (0, 0)
    assert search_matrix(matrix, 17) == (2, 2)

def test_search_matrix_errors():
    """Test error handling"""
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix(None, 5)

def test_search_matrix_not_found():
    """Test cases where target is not in matrix"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 0) is None
    assert search_matrix(matrix, 18) is None
    assert search_matrix(matrix, 10) is None
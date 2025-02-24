import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic_present():
    """Test searching for a value present in the matrix"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 60) == True
    assert search_matrix(matrix, 13) == False

def test_matrix_search_edge_cases():
    """Test various edge cases"""
    # Single element matrix
    matrix1 = [[5]]
    assert search_matrix(matrix1, 5) == True
    assert search_matrix(matrix1, 6) == False

    # Rectangular matrix
    matrix2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert search_matrix(matrix2, 4) == True
    assert search_matrix(matrix2, 7) == False

def test_matrix_search_large_matrix():
    """Test with a larger matrix"""
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_matrix(matrix, 5) == True
    assert search_matrix(matrix, 20) == False

def test_matrix_search_error_handling():
    """Test error handling for invalid inputs"""
    # Empty matrix
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    # Matrix with empty rows
    with pytest.raises(ValueError):
        search_matrix([[], []], 5)

def test_matrix_search_boundary_values():
    """Test boundary values at the matrix edges"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 1) == True  # First element
    assert search_matrix(matrix, 17) == True  # Last element
    assert search_matrix(matrix, 0) == False  # Below first element
    assert search_matrix(matrix, 18) == False  # Above last element
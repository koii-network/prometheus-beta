import pytest
from src.matrix_search import search_matrix

def test_search_matrix():
    # Test case 1: Target exists in matrix
    matrix1 = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_matrix(matrix1, 5) == True
    assert search_matrix(matrix1, 20) == False

def test_empty_matrix():
    # Test case 2: Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[]], 5) == False

def test_single_element_matrix():
    # Test case 3: Single element matrix
    matrix2 = [[1]]
    assert search_matrix(matrix2, 1) == True
    assert search_matrix(matrix2, 2) == False

def test_rectangular_matrix():
    # Test case 4: Non-square matrix
    matrix3 = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17],
        [19, 21, 23]
    ]
    assert search_matrix(matrix3, 9) == True
    assert search_matrix(matrix3, 8) == False

def test_edge_cases():
    # Test case 5: Edge cases
    matrix4 = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert search_matrix(matrix4, 1) == True  # First element
    assert search_matrix(matrix4, 9) == True  # Last element
    assert search_matrix(matrix4, 10) == False  # Out of range
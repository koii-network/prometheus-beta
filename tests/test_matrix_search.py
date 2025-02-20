import pytest
from src.matrix_search import search_matrix

def test_basic_matrix_search():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    
    # Test successful search
    assert search_matrix(matrix, 9) == (True, (1, 1))
    assert search_matrix(matrix, 1) == (True, (0, 0))
    assert search_matrix(matrix, 17) == (True, (2, 2))
    
    # Test unsuccessful search
    assert search_matrix(matrix, 2) == (False, (-1, -1))
    assert search_matrix(matrix, 100) == (False, (-1, -1))

def test_empty_matrix():
    # Test empty matrix scenarios
    assert search_matrix([], 5) == (False, (-1, -1))
    assert search_matrix([[]], 5) == (False, (-1, -1))

def test_search_with_constraints():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    
    # Test row-wise search (default)
    assert search_matrix(matrix, 9, {'row_wise': True}) == (True, (1, 1))
    
    # Test column-wise search
    assert search_matrix(matrix, 7, {'row_wise': False}) == (True, (1, 0))

def test_strictly_increasing_matrix():
    # Matrix with strictly increasing rows and columns
    matrix = [
        [1, 3, 5],
        [2, 4, 6],
        [7, 8, 9]
    ]
    
    # Should pass strictly increasing check
    assert search_matrix(matrix, 4, {'strictly_increasing': True}) == (True, (1, 1))
    
    # Matrix not strictly increasing
    invalid_matrix = [
        [1, 3, 2],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Should fail strictly increasing check
    assert search_matrix(invalid_matrix, 2, {'strictly_increasing': True}) == (False, (-1, -1))

def test_max_iterations():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    
    # Set max iterations to less than needed
    assert search_matrix(matrix, 17, {'max_iterations': 5}) == (False, (-1, -1))
    assert search_matrix(matrix, 17, {'max_iterations': 8}) == (True, (2, 2))

def test_multiple_constraints():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    
    # Multiple constraints
    assert search_matrix(matrix, 9, {
        'row_wise': True, 
        'strictly_increasing': True,
        'max_iterations': 10
    }) == (True, (1, 1))
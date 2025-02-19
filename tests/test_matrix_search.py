import pytest
from src.matrix_search import search_matrix

def test_matrix_search_present():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 17) == True

def test_matrix_search_not_present():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 4) == False
    assert search_matrix(matrix, 12) == False
    assert search_matrix(matrix, 20) == False

def test_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[]], 5) == False
    
    # Single element matrix
    assert search_matrix([[7]], 7) == True
    assert search_matrix([[7]], 8) == False

def test_matrix_unique_elements_validation():
    # Matrix with duplicate elements should raise ValueError
    duplicate_matrix = [
        [1, 2, 3],
        [4, 2, 6],
        [7, 8, 9]
    ]
    with pytest.raises(ValueError, match="Matrix must contain unique integers"):
        search_matrix(duplicate_matrix, 5)

def test_matrix_search_large_matrix():
    large_matrix = [
        [x for x in range(1, 101)],
        [x for x in range(101, 201)],
        [x for x in range(201, 301)]
    ]
    assert search_matrix(large_matrix, 50) == True
    assert search_matrix(large_matrix, 150) == True
    assert search_matrix(large_matrix, 250) == True
    assert search_matrix(large_matrix, 0) == False
    assert search_matrix(large_matrix, 302) == False
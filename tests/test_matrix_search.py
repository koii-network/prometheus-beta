import pytest
from src.matrix_search import matrix_search

def test_matrix_search_basic():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_search(matrix, 5) == (1, 1)
    assert matrix_search(matrix, 9) == (2, 2)
    assert matrix_search(matrix, 1) == (0, 0)

def test_matrix_search_not_found():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_search(matrix, 10) is None

def test_matrix_search_single_element_matrix():
    matrix = [[42]]
    assert matrix_search(matrix, 42) == (0, 0)
    assert matrix_search(matrix, 43) is None

def test_matrix_search_single_row_matrix():
    matrix = [[1, 2, 3, 4]]
    assert matrix_search(matrix, 3) == (0, 2)
    assert matrix_search(matrix, 5) is None

def test_matrix_search_single_column_matrix():
    matrix = [[1], [2], [3], [4]]
    assert matrix_search(matrix, 3) == (2, 0)
    assert matrix_search(matrix, 5) is None

def test_matrix_search_invalid_input():
    with pytest.raises(ValueError, match="Matrix must be a non-empty 2D list"):
        matrix_search([], 5)
    
    with pytest.raises(ValueError, match="Matrix must be a non-empty 2D list"):
        matrix_search(None, 5)

def test_matrix_search_inconsistent_rows():
    with pytest.raises(ValueError, match="All rows in the matrix must have the same length"):
        matrix_search([[1, 2], [3]], 5)

def test_matrix_search_invalid_matrix_type():
    with pytest.raises(TypeError, match="Input must be a 2D matrix"):
        matrix_search([1, 2, 3], 5)
    
    with pytest.raises(TypeError, match="Input must be a 2D matrix"):
        matrix_search([[1], [2, 3]], 5)
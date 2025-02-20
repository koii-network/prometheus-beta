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

def test_matrix_search_single_element():
    matrix = [[42]]
    assert matrix_search(matrix, 42) == (0, 0)
    assert matrix_search(matrix, 43) is None

def test_matrix_search_multiple_rows_cols():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert matrix_search(matrix, 7) == (1, 2)
    assert matrix_search(matrix, 12) == (2, 3)

def test_matrix_search_error_cases():
    # Empty matrix
    with pytest.raises(TypeError):
        matrix_search([], 5)
    
    # Non-list input
    with pytest.raises(TypeError):
        matrix_search("not a matrix", 5)
    
    # Inconsistent row lengths
    with pytest.raises(TypeError):
        matrix_search([[1, 2], [3]], 2)
    
    # Empty rows
    matrix_with_empty_rows = [[], [1, 2], [3, 4]]
    assert matrix_search(matrix_with_empty_rows, 1) is None
import pytest
from src.matrix_search import matrix_search

def test_matrix_search_found():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_search(matrix, 5) == (1, 1)
    assert matrix_search(matrix, 1) == (0, 0)
    assert matrix_search(matrix, 9) == (2, 2)

def test_matrix_search_not_found():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_search(matrix, 10) is None

def test_matrix_search_empty_matrix():
    assert matrix_search([], 5) is None
    assert matrix_search([[]], 5) is None

def test_matrix_search_invalid_input():
    with pytest.raises(TypeError):
        matrix_search("not a matrix", 5)
    
    with pytest.raises(TypeError):
        matrix_search(None, 5)

def test_matrix_search_non_uniform_rows():
    matrix = [
        [1, 2, 3],
        [4, 5],
        [7, 8, 9]
    ]
    with pytest.raises(ValueError):
        matrix_search(matrix, 5)

def test_matrix_search_different_types():
    matrix = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    assert matrix_search(matrix, 'e') == (1, 1)
    assert matrix_search(matrix, 'x') is None
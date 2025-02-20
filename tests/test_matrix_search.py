import pytest
from src.matrix_search import matrix_search

def test_matrix_search_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_search(matrix, 5) == (1, 1)
    assert matrix_search(matrix, 9) == (2, 2)
    assert matrix_search(matrix, 1) == (0, 0)

def test_matrix_search_not_found():
    """Test when target is not in the matrix"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_search(matrix, 10) is None

def test_matrix_search_empty():
    """Test empty matrix"""
    assert matrix_search([], 1) is None
    assert matrix_search([[]], 1) is None

def test_matrix_search_single_element():
    """Test matrix with single element"""
    matrix = [[42]]
    assert matrix_search(matrix, 42) == (0, 0)
    assert matrix_search(matrix, 43) is None

def test_matrix_search_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        matrix_search("not a matrix", 1)
    with pytest.raises(TypeError):
        matrix_search([1, 2, 3], 1)
    with pytest.raises(TypeError):
        matrix_search([[1, 2], [3, []]], 4)
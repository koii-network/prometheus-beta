import pytest
from src.matrix_search import search_sorted_matrix

def test_basic_matrix_search():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 13) == False

def test_single_row_matrix():
    matrix = [[1, 3, 5]]
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 4) == False

def test_single_column_matrix():
    matrix = [[1], [3], [5]]
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 4) == False

def test_empty_matrix():
    matrix = []
    assert search_sorted_matrix(matrix, 5) == False

def test_matrix_with_empty_row():
    matrix = [[], [1, 2, 3]]
    assert search_sorted_matrix(matrix, 2) == True
    assert search_sorted_matrix(matrix, 5) == False

def test_edge_cases():
    matrix = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert search_sorted_matrix(matrix, 1) == True
    assert search_sorted_matrix(matrix, 9) == True
    assert search_sorted_matrix(matrix, 0) == False
    assert search_sorted_matrix(matrix, 10) == False

def test_invalid_input_types():
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_sorted_matrix("not a matrix", 5)
    
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_sorted_matrix([[1, 2], [3, 4]], "not an int")

def test_unsorted_matrix():
    unsorted_matrix = [
        [5, 3, 1],
        [10, 11, 16]
    ]
    with pytest.raises(ValueError, match="Inner lists must be sorted in ascending order"):
        search_sorted_matrix(unsorted_matrix, 3)
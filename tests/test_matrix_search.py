import pytest
from src.matrix_search import search_matrix

def test_target_exists_in_matrix():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 9) == True

def test_target_does_not_exist_in_matrix():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 10) == False

def test_target_in_first_row():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 3) == True

def test_target_in_last_row():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 17) == True

def test_empty_matrix():
    matrix = []
    assert search_matrix(matrix, 5) == False

def test_matrix_with_empty_row():
    matrix = [[]]
    assert search_matrix(matrix, 5) == False

def test_single_element_matrix_target_exists():
    matrix = [[5]]
    assert search_matrix(matrix, 5) == True

def test_single_element_matrix_target_not_exists():
    matrix = [[5]]
    assert search_matrix(matrix, 6) == False

def test_invalid_matrix_type():
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_matrix("not a matrix", 5)

def test_invalid_row_type():
    with pytest.raises(TypeError, match="Each row must be a list"):
        search_matrix([1, 2, 3], 5)

def test_invalid_element_type():
    with pytest.raises(ValueError, match="Matrix must contain only integers"):
        search_matrix([[1, 2, "3"]], 3)

def test_invalid_target_type():
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_matrix([[1, 2, 3]], "5")
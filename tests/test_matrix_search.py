import pytest
from src.matrix_search import search_matrix

def test_matrix_search_present_first_element():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 1) == True

def test_matrix_search_present_last_element():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 17) == True

def test_matrix_search_present_middle_element():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 9) == True

def test_matrix_search_not_present():
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix, 10) == False

def test_matrix_search_edge_case_single_element_present():
    matrix = [[5]]
    assert search_matrix(matrix, 5) == True

def test_matrix_search_edge_case_single_element_not_present():
    matrix = [[5]]
    assert search_matrix(matrix, 6) == False

def test_matrix_search_raise_value_error_empty_matrix():
    with pytest.raises(ValueError):
        search_matrix([], 5)

def test_matrix_search_raise_value_error_empty_rows():
    with pytest.raises(ValueError):
        search_matrix([[], [], []], 5)
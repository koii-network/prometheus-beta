import pytest
from src.matrix_search import search_matrix

def test_search_matrix_found():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[], [], []], 5) == False

    # Single row matrix
    single_row_matrix = [[1, 2, 3]]
    assert search_matrix(single_row_matrix, 2) == True
    assert search_matrix(single_row_matrix, 4) == False

    # Single column matrix
    single_col_matrix = [[1], [3], [5]]
    assert search_matrix(single_col_matrix, 3) == True
    assert search_matrix(single_col_matrix, 4) == False

def test_search_matrix_invalid_inputs():
    # Invalid matrix types
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_matrix("not a matrix", 5)
    
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        search_matrix([1, 2, 3], 5)

    # Invalid target type
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_matrix([[1, 2], [3, 4]], "5")
    
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_matrix([[1, 2], [3, 4]], 5.5)

def test_search_matrix_invalid_matrix_structure():
    # Non-integer elements
    with pytest.raises(ValueError, match="Matrix must contain only integers"):
        search_matrix([[1, 2], [3, "4"]], 3)

    # Unsorted rows
    with pytest.raises(ValueError, match="Rows must be sorted in ascending order"):
        search_matrix([[3, 1], [4, 5]], 3)

def test_search_matrix_large_matrix():
    large_matrix = [
        [x for x in range(i*10, (i+1)*10)] for i in range(10)
    ]
    for x in range(100):
        assert search_matrix(large_matrix, x) == True
    
    assert search_matrix(large_matrix, 100) == False
    assert search_matrix(large_matrix, -1) == False
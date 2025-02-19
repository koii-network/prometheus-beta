import pytest
from src.matrix_search import search_matrix

def test_matrix_search():
    # Test case 1: Target present in matrix
    matrix1 = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix1, 9) == True
    assert search_matrix(matrix1, 1) == True
    assert search_matrix(matrix1, 17) == True

    # Test case 2: Target not present in matrix
    matrix2 = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    assert search_matrix(matrix2, 5) == False
    assert search_matrix(matrix2, 13) == False
    assert search_matrix(matrix2, 19) == False

    # Test case 3: Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[]], 5) == False

    # Test case 4: Matrix with single element
    matrix3 = [[42]]
    assert search_matrix(matrix3, 42) == True
    assert search_matrix(matrix3, 43) == False

def test_matrix_search_type_safety():
    # Test type safety
    matrix4 = [[1, 2], [3, 4]]
    
    # Ensure function doesn't raise exception with different types
    with pytest.raises(TypeError):
        search_matrix(matrix4, "5")
    
    with pytest.raises(TypeError):
        search_matrix(matrix4, None)
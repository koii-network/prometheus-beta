import pytest
from src.matrix_search import find_matrix_coordinates

def test_find_matrix_coordinates_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)

def test_find_matrix_coordinates_first_last():
    """Test finding first and last elements"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 1) == (0, 0)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)

def test_find_matrix_coordinates_not_found():
    """Test when target is not in the matrix"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 10) is None

def test_find_matrix_coordinates_empty_matrix():
    """Test error handling for empty matrix"""
    with pytest.raises(ValueError, match="Matrix must be a non-empty list of lists"):
        find_matrix_coordinates([], 5)

def test_find_matrix_coordinates_invalid_matrix():
    """Test error handling for invalid matrix structure"""
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        find_matrix_coordinates([1, 2, 3], 5)
    
    with pytest.raises(ValueError, match="All rows in the matrix must have the same length"):
        find_matrix_coordinates([[1, 2], [3, 4, 5]], 5)

def test_find_matrix_coordinates_different_types():
    """Test matrix search with different value types"""
    matrix = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    assert find_matrix_coordinates(matrix, 'e') == (1, 1)
    assert find_matrix_coordinates(matrix, 'x') is None
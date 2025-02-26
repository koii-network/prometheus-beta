import pytest
from src.matrix_search import find_matrix_coordinates

def test_find_matrix_coordinates_basic():
    """Test basic functionality of finding coordinates in a matrix."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 1) == (0, 0)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)

def test_find_matrix_coordinates_not_found():
    """Test when target is not in the matrix."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 10) is None

def test_find_matrix_coordinates_first_occurrence():
    """Test that the first occurrence is returned when multiple exist."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [5, 5, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)

def test_find_matrix_coordinates_empty_matrix():
    """Test error handling for empty matrix."""
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        find_matrix_coordinates([], 5)
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        find_matrix_coordinates([[], [], []], 5)

def test_find_matrix_coordinates_invalid_input():
    """Test error handling for invalid input types."""
    # Not a 2D list
    with pytest.raises(TypeError, match="Input must be a 2D list"):
        find_matrix_coordinates("not a matrix", 5)
    
    # Inconsistent row lengths
    with pytest.raises(ValueError, match="All rows in the matrix must have the same length"):
        find_matrix_coordinates([[1,2], [3,4,5]], 5)
    
    # Non-integer values
    with pytest.raises(TypeError, match="Matrix must contain only integer values"):
        find_matrix_coordinates([[1,2], ['a','b']], 5)

def test_find_matrix_coordinates_large_matrix():
    """Test with a larger matrix."""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    assert find_matrix_coordinates(matrix, 11) == (2, 2)
    assert find_matrix_coordinates(matrix, 16) == (3, 3)
    assert find_matrix_coordinates(matrix, 1) == (0, 0)

def test_find_matrix_coordinates_edge_cases():
    """Test various edge cases."""
    # Single element matrix
    assert find_matrix_coordinates([[5]], 5) == (0, 0)
    assert find_matrix_coordinates([[5]], 6) is None

    # Single row matrix
    assert find_matrix_coordinates([[1, 2, 3]], 2) == (0, 1)
    
    # Single column matrix
    matrix = [[1], [2], [3]]
    assert find_matrix_coordinates(matrix, 2) == (1, 0)
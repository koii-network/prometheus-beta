import pytest
from src.matrix_search import search_matrix

def test_target_in_matrix():
    """Test finding a target that exists in the matrix"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_matrix_edges():
    """Test matrix edge cases"""
    # Single element matrix
    assert search_matrix([[1]], 1) == True
    assert search_matrix([[1]], 2) == False
    
    # Single row matrix
    assert search_matrix([[1, 3, 5]], 3) == True
    assert search_matrix([[1, 3, 5]], 4) == False
    
    # Single column matrix
    assert search_matrix([[1], [3], [5]], 3) == True
    assert search_matrix([[1], [3], [5]], 4) == False

def test_empty_matrix():
    """Test empty matrix scenarios"""
    assert search_matrix([], 5) == False
    assert search_matrix([[], []], 5) == False

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        search_matrix("not a matrix", 5)
    
    with pytest.raises(TypeError):
        search_matrix([[1, 2], ["not", "int"]], 5)

def test_large_matrix():
    """Test large matrix with various search scenarios"""
    large_matrix = [
        [x for x in range(i*10, (i+1)*10)] for i in range(100)
    ]
    
    # Test targets at various positions
    assert search_matrix(large_matrix, 0) == True
    assert search_matrix(large_matrix, 999) == True
    assert search_matrix(large_matrix, 1000) == False
    assert search_matrix(large_matrix, -1) == False
import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Test finding an existing value
    found, pos = search_matrix(matrix, 5)
    assert found is True
    assert pos == [1, 1]
    
    # Test value not in matrix
    found, pos = search_matrix(matrix, 10)
    assert found is False
    assert pos == []

def test_search_matrix_constraints():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    # Test row constraint
    found, pos = search_matrix(matrix, 7, {'direction': 'row', 'start_row': 1, 'end_row': 1})
    assert found is True
    assert pos == [1, 2]
    
    # Test column constraint
    found, pos = search_matrix(matrix, 14, {'direction': 'column', 'start_col': 1, 'end_col': 1})
    assert found is True
    assert pos == [3, 1]
    
    # Test region constraint
    found, pos = search_matrix(matrix, 12, {
        'start_row': 1, 'end_row': 2, 
        'start_col': 2, 'end_col': 3
    })
    assert found is True
    assert pos == [2, 3]

def test_search_matrix_edge_cases():
    # Empty matrix
    found, pos = search_matrix([], 5)
    assert found is False
    assert pos == []
    
    # Empty row matrix
    found, pos = search_matrix([[], []], 5)
    assert found is False
    assert pos == []

def test_search_matrix_invalid_constraints():
    matrix = [[1, 2], [3, 4]]
    
    # Invalid row constraints
    with pytest.raises(ValueError):
        search_matrix(matrix, 3, {'start_row': -1, 'end_row': 2})
    
    # Invalid column constraints
    with pytest.raises(ValueError):
        search_matrix(matrix, 3, {'start_col': 0, 'end_col': 3})
    
    # Start greater than end
    with pytest.raises(ValueError):
        search_matrix(matrix, 3, {'start_row': 1, 'end_row': 0})

def test_search_matrix_large():
    # Large matrix to test performance
    matrix = [[i * cols + j for j in range(100)] for i in range(100)]
    
    # Search near the end
    found, pos = search_matrix(matrix, 9999)
    assert found is True
    assert pos == [99, 99]
    
    # Search near the beginning
    found, pos = search_matrix(matrix, 0)
    assert found is True
    assert pos == [0, 0]
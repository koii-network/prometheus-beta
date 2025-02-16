import sys
import pytest
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_basic():
    # Basic graph with known shortest paths
    graph = [
        [0, 5, sys.maxsize, 10],
        [sys.maxsize, 0, 3, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    
    expected = [
        [0, 5, 8, 9],
        [sys.maxsize, 0, 3, 4],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_complete_graph():
    # Complete graph with direct connections
    graph = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    
    expected = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_disconnected_graph():
    # Graph with some disconnected vertices
    graph = [
        [0, 4, sys.maxsize],
        [4, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    
    expected = [
        [0, 4, sys.maxsize],
        [4, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_empty_graph_raises_error():
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_floyd_warshall_non_square_matrix_raises_error():
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])
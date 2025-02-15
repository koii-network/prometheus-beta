import pytest
import sys
from src.floyd_warshall import floyd_warshall, reconstruct_path

def test_floyd_warshall_basic():
    # Simple graph with known shortest paths
    graph = [
        [0, 5, sys.maxsize, 10],
        [sys.maxsize, 0, 3, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    
    dist, next_matrix = floyd_warshall(graph)
    
    # Expected shortest distances
    expected_dist = [
        [0, 5, 8, 9],
        [sys.maxsize, 0, 3, 4],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    
    assert dist == expected_dist

def test_floyd_warshall_path_reconstruction():
    graph = [
        [0, 5, sys.maxsize, 10],
        [sys.maxsize, 0, 3, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    
    _, next_matrix = floyd_warshall(graph)
    
    # Test path from 0 to 2
    path = reconstruct_path(next_matrix, 0, 2)
    assert path == [0, 1, 2]
    
    # Test path from 0 to 3
    path = reconstruct_path(next_matrix, 0, 3)
    assert path == [0, 1, 2, 3]

def test_floyd_warshall_invalid_input():
    # Test with invalid input
    with pytest.raises(ValueError):
        floyd_warshall([])
    
    with pytest.raises(ValueError):
        floyd_warshall([[1], [2, 3]])

def test_floyd_warshall_no_path():
    # Graph with no path between some nodes
    graph = [
        [0, 5, sys.maxsize],
        [sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    
    dist, next_matrix = floyd_warshall(graph)
    
    # Verify no path between node 0 and node 2
    path = reconstruct_path(next_matrix, 0, 2)
    assert path is None
import pytest
import sys
import math
from src.floyd_warshall import floyd_warshall, reconstruct_path

def test_floyd_warshall_simple_graph():
    # Simple graph with direct paths
    graph = [
        [0, 5, float('inf')],
        [5, 0, 3],
        [float('inf'), 3, 0]
    ]
    
    expected = [
        [0, 5, 8],
        [5, 0, 3],
        [8, 3, 0]
    ]
    
    result = floyd_warshall(graph)
    
    for i in range(len(graph)):
        for j in range(len(graph)):
            assert math.isclose(result[i][j], expected[i][j], abs_tol=1e-9)

def test_floyd_warshall_empty_graph():
    # Test empty graph raises ValueError
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_floyd_warshall_non_square_matrix():
    # Test non-square matrix raises ValueError
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_reconstruct_path_simple():
    # Distance matrix from a simple graph
    graph = [
        [0, 5, 8],
        [5, 0, 3],
        [8, 3, 0]
    ]
    
    # Path from node 0 to node 2
    path = reconstruct_path(graph, 0, 2)
    assert path == [0, 2]  # Direct path
    
    # Path from node 0 to node 1
    path = reconstruct_path(graph, 0, 1)
    assert path == [0, 1]  # Direct path

def test_reconstruct_path_no_path():
    # Graph with no path between some nodes
    graph = [
        [0, float('inf'), float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    
    # Test path between disconnected nodes
    path = reconstruct_path(graph, 0, 2)
    assert path is None

def test_reconstruct_path_invalid_indices():
    # Distance matrix
    graph = [
        [0, 5, 8],
        [5, 0, 3],
        [8, 3, 0]
    ]
    
    # Test out of bounds indices
    with pytest.raises(ValueError, match="Start or end indices out of bounds"):
        reconstruct_path(graph, -1, 2)
    
    with pytest.raises(ValueError, match="Start or end indices out of bounds"):
        reconstruct_path(graph, 0, 3)

def test_reconstruct_path_same_node():
    # Distance matrix
    graph = [
        [0, 5, 8],
        [5, 0, 3],
        [8, 3, 0]
    ]
    
    # Test path to same node
    path = reconstruct_path(graph, 1, 1)
    assert path == [1]
import pytest
import sys
import math
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_basic():
    # Simple graph with known shortest paths
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    expected = [
        [0, 5, 8, 9],
        [float('inf'), 0, 3, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_disconnected():
    # Graph with some disconnected vertices
    graph = [
        [0, 4, float('inf')],
        [float('inf'), 0, 8],
        [float('inf'), float('inf'), 0]
    ]
    
    expected = [
        [0, 4, 12],
        [float('inf'), 0, 8],
        [float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_single_vertex():
    # Single vertex graph
    graph = [[0]]
    
    result = floyd_warshall(graph)
    assert result == [[0]]

def test_floyd_warshall_invalid_input():
    # Empty graph
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])
    
    # Non-square matrix
    with pytest.raises(ValueError, match="Input must be a square adjacency matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_floyd_warshall_negative_weights():
    # Graph with negative weights (but no negative cycles)
    graph = [
        [0, -1, 4],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    
    expected = [
        [0, -1, 2],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected
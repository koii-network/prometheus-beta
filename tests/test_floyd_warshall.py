import pytest
import sys
import math
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_basic_graph():
    # Basic graph with known shortest paths
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
    assert result == expected, f"Expected {expected}, but got {result}"

def test_floyd_warshall_disconnected_vertices():
    # Graph with some disconnected vertices
    graph = [
        [0, 4, float('inf')],
        [float('inf'), 0, 1],
        [float('inf'), float('inf'), 0]
    ]
    
    expected = [
        [0, 4, 5],
        [float('inf'), 0, 1],
        [float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_floyd_warshall_invalid_input():
    # Invalid input: non-square matrix
    with pytest.raises(ValueError, match="Input graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_floyd_warshall_single_vertex():
    # Single vertex graph
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]], f"Expected [[0]], but got {result}"

def test_floyd_warshall_negative_weights():
    # Graph with negative edge weights (without negative cycles)
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
    assert result == expected, f"Expected {expected}, but got {result}"
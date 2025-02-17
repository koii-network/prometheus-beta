import pytest
import sys
from src.floyd_warshall import floyd_warshall

def test_basic_shortest_path():
    # Basic graph with known shortest paths
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    
    # Expected shortest paths
    expected = [
        [0, 5, 8, 9],
        [float('inf'), 0, 3, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    assert result == expected

def test_empty_graph():
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_non_square_matrix():
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_single_node_graph():
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]]

def test_fully_connected_graph():
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    
    result = floyd_warshall(graph)
    
    # Expected result with known shortest paths
    expected = [
        [0, 1, 3],
        [1, 0, 2],
        [3, 2, 0]
    ]
    
    assert result == expected
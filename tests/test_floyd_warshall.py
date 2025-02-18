import sys
import pytest
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_basic_graph():
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
    assert result == expected, "Failed to compute correct shortest paths"

def test_floyd_warshall_single_vertex():
    # Single vertex graph
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]], "Failed to handle single vertex graph"

def test_floyd_warshall_empty_graph():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_floyd_warshall_non_square_matrix():
    # Non-square matrix should raise ValueError
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_floyd_warshall_no_path_graph():
    # Graph with no paths between some vertices
    graph = [
        [0, sys.maxsize, sys.maxsize],
        [sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == graph, "Failed to handle graph with no direct paths"
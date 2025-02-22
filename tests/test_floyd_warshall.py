import sys
import pytest
from src.floyd_warshall import floyd_warshall

def test_basic_shortest_path():
    # Simple graph with known shortest paths
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

def test_empty_graph():
    assert floyd_warshall([]) is None
    assert floyd_warshall([[]]) is None

def test_single_node_graph():
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]]

def test_disconnected_graph():
    graph = [
        [0, 5, sys.maxsize],
        [5, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    
    expected = [
        [0, 5, sys.maxsize],
        [5, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_negative_cycle():
    # Graph with a negative cycle
    graph = [
        [0, 1, sys.maxsize],
        [sys.maxsize, 0, -3],
        [-1, sys.maxsize, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result is None
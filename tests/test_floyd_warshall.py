import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from floyd_warshall import floyd_warshall

def test_floyd_warshall_simple_graph():
    # Test a simple graph with known shortest paths
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

def test_floyd_warshall_disconnected_graph():
    # Test a graph with some disconnected nodes
    graph = [
        [0, 4, float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    
    # Nodes that remain disconnected should have float('inf')
    expected = [
        [0, 4, float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    
    assert result == expected

def test_floyd_warshall_single_node():
    # Test a graph with a single node
    graph = [[0]]
    
    result = floyd_warshall(graph)
    
    assert result == [[0]]

def test_floyd_warshall_negative_paths():
    # Test a graph with some negative paths
    graph = [
        [0, -1, 4],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    
    # Expected shortest paths, including paths through intermediate nodes
    expected = [
        [0, -1, 2],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    
    assert result == expected
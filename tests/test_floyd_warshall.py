import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from floyd_warshall import floyd_warshall

def test_floyd_warshall_basic():
    # Basic graph with 3 vertices
    graph = [
        [0, 5, float('inf')],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, 5, 8],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_disconnected():
    # Graph with disconnected vertices
    graph = [
        [0, float('inf'), float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, float('inf'), float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_complex():
    # More complex graph with multiple paths
    graph = [
        [0, 4, float('inf'), float('inf')],
        [float('inf'), 0, 8, float('inf')],
        [float('inf'), float('inf'), 0, 7],
        [float('inf'), float('inf'), 9, 0]
    ]
    expected = [
        [0, 4, 12, 19],
        [float('inf'), 0, 8, 15],
        [float('inf'), float('inf'), 0, 7],
        [float('inf'), float('inf'), 9, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_single_vertex():
    # Single vertex graph
    graph = [[0]]
    expected = [[0]]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_input_validation():
    # Test that the function handles empty graph
    with pytest.raises(IndexError):
        floyd_warshall([])
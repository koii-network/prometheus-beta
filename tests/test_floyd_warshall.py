import pytest
import sys
from src.floyd_warshall import floyd_warshall

def test_floyd_warshall_basic():
    """Test a basic graph with known shortest paths."""
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

def test_floyd_warshall_self_loops():
    """Test a graph with self-loops."""
    graph = [
        [0, 1, float('inf')],
        [1, 0, 2],
        [float('inf'), 2, 0]
    ]
    expected = [
        [0, 1, 3],
        [1, 0, 2],
        [3, 2, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_disconnected():
    """Test a graph with disconnected nodes."""
    graph = [
        [0, 1, float('inf')],
        [1, 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, 1, float('inf')],
        [1, 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_floyd_warshall_empty_graph():
    """Test an empty graph."""
    result = floyd_warshall([])
    assert result is None

def test_floyd_warshall_invalid_input():
    """Test an invalid input (non-square matrix)."""
    with pytest.raises(ValueError):
        floyd_warshall([
            [0, 1, 2],
            [1, 0]
        ])

def test_floyd_warshall_negative_weight_cycle():
    """Test a graph with a negative weight cycle."""
    graph = [
        [0, 1, float('inf')],
        [1, 0, -3],
        [-3, float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result is None
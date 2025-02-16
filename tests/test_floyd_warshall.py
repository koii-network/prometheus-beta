import pytest
import sys
import math

# Ensure the src directory is in the Python path
sys.path.append('src')

from floyd_warshall import floyd_warshall

def test_basic_graph():
    """Test a basic graph with known shortest path results."""
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

def test_fully_connected_graph():
    """Test a fully connected graph."""
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    expected = [
        [0, 1, 3],
        [1, 0, 2],
        [3, 2, 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == expected

def test_empty_graph():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError, match="Input graph cannot be empty"):
        floyd_warshall([])

def test_non_square_matrix():
    """Test that a non-square matrix raises a ValueError."""
    non_square_graph = [
        [0, 1, 2],
        [3, 4]
    ]
    
    with pytest.raises(ValueError, match="Input graph must be a square matrix"):
        floyd_warshall(non_square_graph)

def test_infinite_connections():
    """Test a graph with only infinite connections."""
    graph = [
        [0, float('inf'), float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    
    result = floyd_warshall(graph)
    assert result == graph
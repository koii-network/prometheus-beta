import pytest
import math
from src.floyd_warshall import floyd_warshall, reconstruct_path

def test_floyd_warshall_basic():
    """Test basic Floyd-Warshall algorithm with a simple graph."""
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    dist, next_matrix = floyd_warshall(graph)
    
    # Expected shortest distances
    expected_dist = [
        [0, 5, 8, 9],
        [float('inf'), 0, 3, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    # Check distances
    for i in range(len(graph)):
        for j in range(len(graph)):
            assert math.isclose(dist[i][j], expected_dist[i][j], 
                                abs_tol=1e-9), f"Failed at [{i}][{j}]"

def test_floyd_warshall_no_path():
    """Test graph with no direct connections."""
    graph = [
        [0, float('inf'), float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    
    dist, next_matrix = floyd_warshall(graph)
    
    # All distances should remain as no path
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                assert dist[i][j] == float('inf')

def test_floyd_warshall_input_validation():
    """Test input validation of the algorithm."""
    # Empty graph
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])
    
    # Non-square matrix
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([[1, 2], [3]])

def test_reconstruct_path():
    """Test path reconstruction."""
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    
    _, next_matrix = floyd_warshall(graph)
    
    # Test existing path
    path = reconstruct_path(next_matrix, 0, 2)
    assert path == [0, 2], "Path from 0 to 2 should be [0, 2]"
    
    path = reconstruct_path(next_matrix, 0, 3)
    assert path == [0, 2, 3], "Path from 0 to 3 should be [0, 2, 3]"

def test_reconstruct_path_no_path():
    """Test path reconstruction when no path exists."""
    graph = [
        [0, float('inf'), float('inf')],
        [float('inf'), 0, float('inf')],
        [float('inf'), float('inf'), 0]
    ]
    
    _, next_matrix = floyd_warshall(graph)
    
    # Test non-existing path
    path = reconstruct_path(next_matrix, 0, 1)
    assert path is None, "Path should be None when no path exists"

def test_reconstruct_path_invalid_input():
    """Test path reconstruction with invalid inputs."""
    graph = [
        [0, 5, float('inf')],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    
    _, next_matrix = floyd_warshall(graph)
    
    # Test out of bounds inputs
    assert reconstruct_path(next_matrix, -1, 0) is None
    assert reconstruct_path(next_matrix, 0, 3) is None
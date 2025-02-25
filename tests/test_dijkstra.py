import pytest
from src.dijkstra import dijkstra

def test_basic_graph():
    """Test Dijkstra's algorithm on a simple graph."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    distances = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }

def test_disconnected_node():
    """Test graph with a disconnected node."""
    graph = {
        'A': {'B': 4},
        'B': {'A': 4},
        'C': {}  # Completely disconnected
    }
    
    distances = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 4,
        'C': float('inf')
    }

def test_negative_weights_raise_error():
    """Ensure error is raised for negative weights."""
    graph = {
        'A': {'B': -1},
        'B': {}
    }
    
    with pytest.raises(ValueError, match="Negative weight"):
        dijkstra(graph, 'A')

def test_non_numeric_weights_raise_error():
    """Ensure error is raised for non-numeric weights."""
    graph = {
        'A': {'B': 'invalid'},
        'B': {}
    }
    
    with pytest.raises(ValueError, match="Invalid weight"):
        dijkstra(graph, 'A')

def test_nonexistent_start_node():
    """Test that an error is raised when start node is not in graph."""
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    
    with pytest.raises(ValueError, match="Start node"):
        dijkstra(graph, 'C')

def test_complex_graph():
    """Test Dijkstra's algorithm on a more complex graph."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5, 'E': 6},
        'D': {'E': 2},
        'E': {}
    }
    
    distances = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,   # A -> C -> B
        'C': 2,   # A -> C
        'D': 6,   # A -> C -> B -> D
        'E': 4    # A -> C -> B -> E
    }

def test_empty_graph():
    """Test Dijkstra's algorithm on an empty graph."""
    graph = {}
    
    with pytest.raises(ValueError, match="Start node"):
        dijkstra(graph, 'A')
import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    """Test a simple graph with a clear shortest path."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4

def test_direct_path():
    """Test when there's a direct path between nodes."""
    graph = {
        'A': {'B': 5, 'C': 2},
        'B': {'C': 1},
        'C': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'C')
    assert path == ['A', 'C']
    assert distance == 2

def test_single_node_path():
    """Test path from a node to itself."""
    graph = {
        'A': {},
        'B': {}
    }
    graph['A']['A'] = 0
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_no_path():
    """Test when no path exists between nodes."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {}
    }
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result is None

def test_invalid_nodes():
    """Test raising error for non-existent nodes."""
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start or end node not in graph"):
        dijkstra_shortest_path(graph, 'A', 'C')
    with pytest.raises(ValueError, match="Start or end node not in graph"):
        dijkstra_shortest_path(graph, 'C', 'B')

def test_complex_graph():
    """Test a more complex graph with multiple potential paths."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5, 'E': 6},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 6
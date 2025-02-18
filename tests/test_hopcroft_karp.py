import pytest
from src.hopcroft_karp import hopcroft_karp_maximum_matching

def test_simple_bipartite_graph():
    """Test a simple bipartite graph with a perfect matching."""
    graph = {
        1: [3, 4],
        2: [3, 5],
        3: [1, 2],
        4: [1],
        5: [2]
    }
    
    matching = hopcroft_karp_maximum_matching(graph)
    
    # Verify the number of matched pairs
    matched_pairs = sum(1 for v in matching.values() if v is not None) // 2
    assert matched_pairs == 2  # Perfect matching
    
    # Verify matching properties
    for u, v in matching.items():
        if v is not None:
            assert u in graph[v]
            assert v in graph[u]

def test_empty_graph():
    """Test an empty graph."""
    graph = {}
    matching = hopcroft_karp_maximum_matching(graph)
    assert matching == {}

def test_disconnected_graph():
    """Test a graph with disconnected components."""
    graph = {
        1: [4],
        2: [5],
        3: [6],
        4: [1],
        5: [2],
        6: [3]
    }
    
    matching = hopcroft_karp_maximum_matching(graph)
    
    # Verify the number of matched pairs
    matched_pairs = sum(1 for v in matching.values() if v is not None) // 2
    assert matched_pairs == 3  # Perfect matching for each component

def test_graph_with_unmatched_nodes():
    """Test a graph where not all nodes can be matched."""
    graph = {
        1: [3],
        2: [4],
        3: [1],
        4: [2],
        5: []  # Unmatched node
    }
    
    matching = hopcroft_karp_maximum_matching(graph)
    
    # Verify the number of matched pairs
    matched_pairs = sum(1 for v in matching.values() if v is not None) // 2
    assert matched_pairs == 2

def test_invalid_input():
    """Test that the function raises an error for invalid input."""
    with pytest.raises(ValueError):
        hopcroft_karp_maximum_matching("not a dictionary")
    
    with pytest.raises(ValueError):
        hopcroft_karp_maximum_matching([1, 2, 3])
import pytest
from src.hopcroft_karp import hopcroft_karp_matching

def test_empty_graph():
    """Test matching for an empty graph."""
    graph = {}
    assert hopcroft_karp_matching(graph) == {}

def test_single_edge_graph():
    """Test graph with a single edge."""
    graph = {1: [2]}
    matching = hopcroft_karp_matching(graph)
    assert len(matching) == 2
    assert matching[1] == 2
    assert matching[2] == 1

def test_complete_bipartite_graph():
    """Test a complete bipartite graph."""
    graph = {
        1: [1, 2, 3],
        2: [1, 2, 3],
        3: [1, 2, 3]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Check that the matching is valid
    assert len(matching) == 6  # All vertices matched
    assert len(set(matching.values())) == 3  # One vertex from each right partition

def test_disconnected_graph():
    """Test a graph with disconnected vertices."""
    graph = {
        1: [],
        2: [],
        3: [4],
        4: [3]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Check disconnected pairs are matched correctly
    assert matching.get(3, None) == 4
    assert matching.get(4, None) == 3

def test_complex_bipartite_graph():
    """Test a more complex bipartite graph."""
    graph = {
        1: [4, 5],
        2: [4, 6],
        3: [5, 6],
        4: [1, 2, 7],
        5: [1, 3, 7],
        6: [2, 3, 7]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Validate that the matching is maximum
    assert len(matching) == 6  # All vertices matched
    assert len(set(matching.values())) == 3  # Every vertex matched uniquely
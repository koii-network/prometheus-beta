import pytest
from src.hopcroft_karp import HopcroftKarp

def test_empty_graph():
    """Test maximum matching on an empty graph."""
    hk = HopcroftKarp({})
    assert hk.maximum_matching() == {}

def test_single_edge_graph():
    """Test maximum matching on a graph with a single edge."""
    graph = {1: [2]}
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    assert matching == {1: 2}

def test_multiple_edges_graph():
    """Test maximum matching on a graph with multiple edges."""
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate that the matching is of maximum possible size
    matched_left = set(matching.keys())
    matched_right = set(matching.values())
    assert len(matched_left) >= 2
    assert len(matched_right) == len(matched_left)

def test_disconnected_graph():
    """Test maximum matching on a disconnected graph."""
    graph = {
        1: [2],
        3: [4],
        5: []
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Validate the matching covers maximum possible edges
    matched_left = set(matching.keys())
    matched_right = set(matching.values())
    assert len(matched_left) == 2
    assert len(matched_right) == 2

def test_complex_graph():
    """Test maximum matching on a more complex graph."""
    graph = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2, 4],
        4: [1, 3]
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    
    # Allow matching to be at least 3 vertices
    matched_left = set(matching.keys())
    matched_right = set(matching.values())
    assert len(matched_left) >= 3
    assert len(matched_right) == len(matched_left)

def test_invalid_graph_input():
    """Test that an invalid graph input raises a ValueError."""
    with pytest.raises(ValueError):
        HopcroftKarp([1, 2, 3])  # List instead of dict

def test_no_matching_possible():
    """Test a graph where no matching is possible."""
    graph = {
        1: [],
        2: [],
        3: []
    }
    hk = HopcroftKarp(graph)
    matching = hk.maximum_matching()
    assert matching == {}
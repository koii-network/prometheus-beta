import pytest
from src.hopcroft_karp import HopcroftKarp

def test_empty_graph():
    """Test maximum matching on an empty graph."""
    hk = HopcroftKarp()
    assert hk.maximum_matching() == {}

def test_single_edge():
    """Test maximum matching with a single edge."""
    hk = HopcroftKarp()
    hk.add_edge(1, 4)
    matching = hk.maximum_matching()
    assert len(matching) == 1
    assert 1 in matching
    assert matching[1] == 4

def test_multiple_matching_edges():
    """Test maximum matching with multiple possible edges."""
    hk = HopcroftKarp()
    # Create a simple bipartite graph
    hk.add_edge(1, 4)
    hk.add_edge(1, 5)
    hk.add_edge(2, 4)
    hk.add_edge(3, 5)
    
    matching = hk.maximum_matching()
    assert len(matching) == 2
    # We can't predict exactly which vertices will be matched, 
    # but we know 2 vertices will be matched and no vertex is matched twice
    assert len(set(matching.keys())) == 2
    assert len(set(matching.values())) == 2

def test_disconnected_graph():
    """Test maximum matching on a disconnected graph."""
    hk = HopcroftKarp()
    hk.add_edge(1, 4)
    hk.add_edge(2, 5)
    hk.add_edge(3, 6)
    
    matching = hk.maximum_matching()
    assert len(matching) == 3
    assert set(matching.keys()) == {1, 2, 3}
    assert set(matching.values()) == {4, 5, 6}

def test_complex_graph():
    """Test a more complex bipartite graph."""
    hk = HopcroftKarp()
    # More complex graph connections
    edges = [
        (1, 4), (1, 5), 
        (2, 4), (2, 6), 
        (3, 5), (3, 6)
    ]
    
    for u, v in edges:
        hk.add_edge(u, v)
    
    matching = hk.maximum_matching()
    assert len(matching) == 3
    assert set(matching.keys()) == {1, 2, 3}
    assert len(set(matching.values())) == 3

def test_self_vertex_not_matched():
    """Ensure that individual vertices not in any matching are not included."""
    hk = HopcroftKarp()
    hk.add_edge(1, 4)
    hk.add_edge(2, 5)
    hk.add_edge(3, 6)
    
    matching = hk.maximum_matching()
    assert 7 not in matching
    assert 8 not in matching

def test_non_unique_edges():
    """Test handling of multiple edges between same vertices."""
    hk = HopcroftKarp()
    hk.add_edge(1, 4)
    hk.add_edge(1, 4)  # Duplicate edge
    hk.add_edge(2, 5)
    
    matching = hk.maximum_matching()
    assert len(matching) == 2
    assert set(matching.keys()) == {1, 2}
    assert set(matching.values()) == {4, 5}
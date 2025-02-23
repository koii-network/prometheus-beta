import pytest
from src.hopcroft_karp import HopcroftKarp


def test_simple_matching():
    """Test a simple bipartite graph with a clear maximum matching."""
    graph = {
        1: [3, 4],
        2: [3, 5],
        3: [1, 2],
        4: [1],
        5: [2]
    }
    left_vertices = {1, 2}
    right_vertices = {3, 4, 5}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    # Validate matching size and properties
    assert len(matching) == 2
    assert set(matching.keys()) <= left_vertices
    assert set(matching.values()) <= right_vertices
    assert len(set(matching.values())) == len(matching)


def test_complete_bipartite_graph():
    """Test a complete bipartite graph where every left vertex can match to every right vertex."""
    graph = {
        1: [3, 4, 5],
        2: [3, 4, 5],
        3: [1, 2],
        4: [1, 2],
        5: [1, 2]
    }
    left_vertices = {1, 2}
    right_vertices = {3, 4, 5}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    # In a complete bipartite graph, we expect all vertices to be matched
    assert len(matching) == min(len(left_vertices), len(right_vertices))


def test_empty_graph():
    """Test graph with no edges."""
    graph = {
        1: [],
        2: [],
        3: [],
        4: []
    }
    left_vertices = {1, 2}
    right_vertices = {3, 4}
    
    hk = HopcroftKarp(graph, left_vertices, right_vertices)
    matching = hk.maximum_matching()
    
    # Empty graph should result in no matching
    assert len(matching) == 0


def test_invalid_graph_same_partition():
    """Test that an invalid graph with vertices in the same partition raises an error."""
    graph = {
        1: [2],
        2: [1]
    }
    left_vertices = {1, 2}
    right_vertices = {3, 4}
    
    with pytest.raises(ValueError, match="Left and right vertex sets must be disjoint"):
        HopcroftKarp(graph, left_vertices, right_vertices)


def test_invalid_graph_edge():
    """Test that an invalid graph with incorrect edge connections raises an error."""
    graph = {
        1: [1],  # Edge within left partition
        2: [3]
    }
    left_vertices = {1, 2}
    right_vertices = {3, 4}
    
    with pytest.raises(ValueError, match="Invalid edge"):
        HopcroftKarp(graph, left_vertices, right_vertices)


def test_empty_partitions():
    """Test that empty partitions raise an error."""
    graph = {}
    left_vertices = set()
    right_vertices = {1, 2}
    
    with pytest.raises(ValueError, match="Both left and right vertex sets must be non-empty"):
        HopcroftKarp(graph, left_vertices, right_vertices)
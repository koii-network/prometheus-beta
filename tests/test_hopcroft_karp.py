import pytest
from src.hopcroft_karp import hopcroft_karp_maximum_matching

def test_empty_graph():
    """Test that an empty graph returns an empty matching."""
    graph = {}
    matching = hopcroft_karp_maximum_matching(graph)
    assert matching == {}

def test_simple_matching():
    """Test a simple bipartite graph with a clear maximum matching."""
    graph = {
        1: [4],
        2: [5],
        3: [6]
    }
    matching = hopcroft_karp_maximum_matching(graph)
    assert len(matching) == 3
    assert set(matching.keys()) == {1, 2, 3}
    assert set(matching.values()) == {4, 5, 6}

def test_multiple_matching_possibilities():
    """Test a graph with multiple possible maximum matchings."""
    graph = {
        1: [3, 4],
        2: [3, 4],
        3: [1, 2],
        4: [1, 2]
    }
    matching = hopcroft_karp_maximum_matching(graph)
    # Verify that we have a valid maximum matching
    assert len(matching) >= 2
    # Each key should be matched to a unique value
    assert len(set(matching.keys())) == len(set(matching.values()))

def test_unequal_graph():
    """Test a graph where right vertices outnumber left vertices."""
    graph = {
        1: [4, 5],
        2: [5, 6],
        3: [6, 7]
    }
    matching = hopcroft_karp_maximum_matching(graph)
    assert len(matching) == 3
    assert set(matching.keys()) == {1, 2, 3}

def test_invalid_input():
    """Test that the function raises an error for invalid input."""
    with pytest.raises(ValueError):
        hopcroft_karp_maximum_matching([])  # Not a dictionary
    
    with pytest.raises(ValueError):
        hopcroft_karp_maximum_matching(None)  # None input

def test_disjoint_sets():
    """Test a graph with disconnected vertices."""
    graph = {
        1: [],
        2: [],
        3: []
    }
    matching = hopcroft_karp_maximum_matching(graph)
    assert matching == {}
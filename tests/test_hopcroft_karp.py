import pytest
from src.hopcroft_karp import hopcroft_karp_matching

def test_basic_matching():
    """Test a simple bipartite graph with a straightforward matching."""
    graph = {
        1: [3, 4],
        2: [3, 5],
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify matching
    assert len(matching) == 4  # 4 nodes should be matched
    assert 1 in matching and matching[1] in [3, 4]
    assert 2 in matching and matching[2] in [3, 5]

def test_no_matching():
    """Test a graph with no possible matching."""
    graph = {
        1: [],
        2: [],
    }
    matching = hopcroft_karp_matching(graph)
    assert len(matching) == 0

def test_complete_matching():
    """Test a graph where every node can be matched."""
    graph = {
        1: [4, 5],
        2: [4, 6],
        3: [5, 6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify each node is matched exactly once
    assert len(matching) == 6  # All 6 nodes should be matched
    assert len(set(matching.values())) == 3  # 3 unique pairs

def test_large_graph():
    """Test a larger graph with multiple possible matchings."""
    graph = {
        1: [4, 5, 6],
        2: [4, 5, 7],
        3: [6, 7, 8],
    }
    matching = hopcroft_karp_matching(graph)
    
    assert len(matching) >= 4  # At least 4 nodes should be matched

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(ValueError):
        hopcroft_karp_matching([1, 2, 3])  # Not a dictionary
    
    with pytest.raises(ValueError):
        hopcroft_karp_matching({1: 2})  # Invalid graph structure

def test_symmetric_matching():
    """Verify that the matching is symmetric."""
    graph = {
        1: [4, 5],
        2: [4, 6],
        3: [5, 6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Check symmetry in matching
    for node, matched_node in matching.items():
        assert matched_node in graph.get(node, [])
        assert node in graph[matched_node] if matched_node in graph else False
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
    assert all(node in matching for node in graph)  # All graph nodes matched
    assert all(matching[node] in graph[node] for node in graph)

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
    
    # Verify each node is matched
    assert all(node in matching for node in graph)
    assert len(set(matching.values())) == len(graph)

def test_large_graph():
    """Test a larger graph with multiple possible matchings."""
    graph = {
        1: [4, 5, 6],
        2: [4, 5, 7],
        3: [6, 7, 8],
    }
    matching = hopcroft_karp_matching(graph)
    
    # All input nodes must be matched
    assert all(node in matching for node in graph)

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(ValueError):
        hopcroft_karp_matching([1, 2, 3])  # Not a dictionary
    
    with pytest.raises(ValueError):
        hopcroft_karp_matching({1: "not a list"})  # Invalid graph structure

def test_symmetric_matching():
    """Verify that the matching is symmetric."""
    graph = {
        1: [4, 5],
        2: [4, 6],
        3: [5, 6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Reverse graph for checking back references
    reverse_graph = {}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in reverse_graph:
                reverse_graph[neighbor] = []
            reverse_graph[neighbor].append(node)
    
    # Check symmetry in matching
    for node, matched_node in matching.items():
        assert matched_node in graph.get(node, [])
        assert node in reverse_graph.get(matched_node, [])

def test_single_node_matching():
    """Test matching with a graph where some nodes have single-node adjacency."""
    graph = {
        1: 3,
        2: 4,
        3: [1, 2],
        4: [1, 2]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify matching
    assert all(node in matching for node in graph)
    assert all(matching[node] in graph[node] if isinstance(graph[node], list) else matching[node] == graph[node] for node in graph)
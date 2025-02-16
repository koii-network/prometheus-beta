import pytest
from src.hopcroft_karp import hopcroft_karp_matching

def test_hopcroft_karp_simple_matching():
    """
    Test a simple bipartite graph with a clear maximum matching.
    """
    graph = {
        1: [3, 4],
        2: [3, 5],
        3: [1, 2],
        4: [1],
        5: [2]
    }
    
    matching = hopcroft_karp_matching(graph)
    
    # Validate matching
    assert matching[1] in [3, 4]
    assert matching[2] in [3, 5]
    assert len(set(v for v in matching.values() if v is not None)) == 2

def test_hopcroft_karp_complete_bipartite():
    """
    Test a complete bipartite graph where every vertex can be matched.
    """
    graph = {
        1: [4, 5, 6],
        2: [4, 5, 6],
        3: [4, 5, 6]
    }
    
    matching = hopcroft_karp_matching(graph)
    
    # Validate matching
    assert len(set(v for v in matching.values() if v is not None)) == 3

def test_hopcroft_karp_empty_graph():
    """
    Test an empty graph.
    """
    graph = {}
    
    matching = hopcroft_karp_matching(graph)
    
    # Validate matching
    assert len(matching) == 0

def test_hopcroft_karp_no_matching():
    """
    Test a graph with no possible matching.
    """
    graph = {
        1: [4],
        2: [5],
        3: [6]
    }
    
    matching = hopcroft_karp_matching(graph)
    
    # Validate matching
    assert sum(1 for v in matching.values() if v is not None) <= 1

def test_hopcroft_karp_unbalanced_graph():
    """
    Test a graph with more vertices in one set than the other.
    """
    graph = {
        1: [4, 5],
        2: [4],
        3: [5]
    }
    
    matching = hopcroft_karp_matching(graph)
    
    # Validate matching
    matched_count = sum(1 for v in matching.values() if v is not None)
    assert matched_count == 2

def test_hopcroft_karp_invalid_graph():
    """
    Test that the function handles an invalid graph structure gracefully.
    """
    with pytest.raises(TypeError):
        hopcroft_karp_matching("not a dictionary")
    
    with pytest.raises(TypeError):
        hopcroft_karp_matching({1: "not a list"})
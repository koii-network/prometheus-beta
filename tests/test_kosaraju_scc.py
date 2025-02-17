import pytest
from src.kosaraju_scc import kosaraju_strongly_connected_components

def test_basic_scc():
    """Test a simple graph with multiple strongly connected components."""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4, 7],
        7: []
    }
    
    scc = kosaraju_strongly_connected_components(graph)
    
    # Check that SCCs are correct (order might vary)
    expected_scc = {frozenset([1, 2, 3]), frozenset([4, 5, 6]), frozenset([7])}
    assert len(scc) == 3
    assert all(frozenset(component) in expected_scc for component in scc)

def test_single_component_graph():
    """Test a graph that is a single strongly connected component."""
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    
    scc = kosaraju_strongly_connected_components(graph)
    
    assert len(scc) == 1
    assert set(scc[0]) == {1, 2, 3}

def test_disconnected_graph():
    """Test a graph with multiple disconnected components."""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    
    scc = kosaraju_strongly_connected_components(graph)
    
    expected_scc = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5])}
    assert len(scc) == 3
    assert all(frozenset(component) in expected_scc for component in scc)

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        kosaraju_strongly_connected_components({})

def test_graph_with_no_edges():
    """Test a graph with nodes but no edges."""
    graph = {1: [], 2: [], 3: []}
    
    scc = kosaraju_strongly_connected_components(graph)
    
    assert len(scc) == 3
    assert all(len(component) == 1 for component in scc)
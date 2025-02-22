import pytest
from src.strongly_connected_components import kosaraju_scc

def test_empty_graph():
    """Test an empty graph returns an empty list of components."""
    assert kosaraju_scc({}) == []

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {1: []}
    result = kosaraju_scc(graph)
    assert len(result) == 1
    assert result[0] == [1]

def test_simple_strongly_connected_component():
    """Test a simple graph with a strongly connected component."""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: []
    }
    result = kosaraju_scc(graph)
    assert len(result) == 2
    assert sorted([sorted(comp) for comp in result]) == [[1, 2, 3], [4], [5]]

def test_multiple_components():
    """Test a graph with multiple strongly connected components."""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5, 7],
        5: [6],
        6: [4],
        7: []
    }
    result = kosaraju_scc(graph)
    assert len(result) == 3
    expected_components = [[1, 2, 3], [4, 5, 6], [7]]
    assert sorted([sorted(comp) for comp in result]) == sorted([sorted(comp) for comp in expected_components])

def test_complex_graph():
    """Test a more complex graph with multiple interconnected components."""
    graph = {
        1: [2],
        2: [3, 4],
        3: [1],
        4: [5],
        5: [6],
        6: [4, 7],
        7: []
    }
    result = kosaraju_scc(graph)
    expected_components = [[1, 2, 3], [4, 5, 6], [7]]
    assert sorted([sorted(comp) for comp in result]) == sorted([sorted(comp) for comp in expected_components])
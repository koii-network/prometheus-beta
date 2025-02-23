import pytest
from src.strongly_connected_components import kosaraju_scc

def test_basic_scc():
    """Test a simple graph with one strongly connected component."""
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    result = kosaraju_scc(graph)
    assert len(result) == 1
    assert set(result[0]) == {1, 2, 3}

def test_multiple_sccs():
    """Test a graph with multiple strongly connected components."""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4],
        7: [8],
        8: [9],
        9: [7]
    }
    result = kosaraju_scc(graph)
    assert len(result) == 3
    # Check if each result is a known SCC
    expected_sccs = [
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    ]
    for component in result:
        assert any(set(component) == scc for scc in expected_sccs)

def test_disconnected_graph():
    """Test a graph with disconnected components."""
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    result = kosaraju_scc(graph)
    assert len(result) == 4

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {1: []}
    result = kosaraju_scc(graph)
    assert len(result) == 1
    assert result[0] == [1]

def test_empty_graph():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError):
        kosaraju_scc({})

def test_none_graph():
    """Test that None graph raises a ValueError."""
    with pytest.raises(ValueError):
        kosaraju_scc(None)

def test_complex_graph():
    """Test a more complex graph with multiple SCCs."""
    graph = {
        0: [1, 3],
        1: [2],
        2: [0],
        3: [4],
        4: [5],
        5: [3, 6],
        6: []
    }
    result = kosaraju_scc(graph)
    # Verify the number and nature of SCCs
    assert len(result) == 3
    scc_sets = [set(scc) for scc in result]
    assert any(set(scc) == {0, 1, 2} for scc in scc_sets)
    assert any(set(scc) == {3, 4, 5} for scc in scc_sets)
    assert any(set(scc) == {6} for scc in scc_sets)
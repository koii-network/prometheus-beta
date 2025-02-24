import pytest
from src.strongly_connected_components import kosaraju_scc

def test_basic_scc():
    """Test a simple graph with one strongly connected component"""
    graph = {
        1: [2],
        2: [3],
        3: [1],
    }
    result = kosaraju_scc(graph)
    assert len(result) == 1
    assert set(result[0]) == {1, 2, 3}

def test_multiple_sccs():
    """Test a graph with multiple strongly connected components"""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4],
        7: []
    }
    result = kosaraju_scc(graph)
    assert len(result) == 3
    # Verify the SCCs
    scc_sets = [set(scc) for scc in result]
    assert {1, 2, 3} in scc_sets
    assert {4, 5, 6} in scc_sets
    assert {7} in scc_sets

def test_empty_graph():
    """Test an empty graph"""
    graph = {}
    result = kosaraju_scc(graph)
    assert result == []

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {1: []}
    result = kosaraju_scc(graph)
    assert len(result) == 1
    assert result[0] == [1]

def test_disconnected_nodes():
    """Test a graph with disconnected nodes"""
    graph = {
        1: [],
        2: [],
        3: []
    }
    result = kosaraju_scc(graph)
    assert len(result) == 3
    # Each node is its own SCC
    result_sets = [set(scc) for scc in result]
    assert {1} in result_sets
    assert {2} in result_sets
    assert {3} in result_sets

def test_none_graph():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="Graph cannot be None"):
        kosaraju_scc(None)

def test_dag_scc():
    """Test a directed acyclic graph"""
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    result = kosaraju_scc(graph)
    # Each node will be its own SCC in a DAG
    assert len(result) == 4
    result_sets = [set(scc) for scc in result]
    assert {4} in result_sets
    assert {2} in result_sets
    assert {3} in result_sets
    assert {1} in result_sets
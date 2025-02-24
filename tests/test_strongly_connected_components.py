import pytest
from src.strongly_connected_components import kosaraju_scc

def test_simple_scc():
    # Simple graph with two SCCs
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4]
    }
    sccs = kosaraju_scc(graph)
    assert len(sccs) == 2
    assert sorted([sorted(scc) for scc in sccs]) == [[1, 2, 3], [4, 5, 6]]

def test_linear_graph():
    # Linear graph (no cycles)
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [5]
    }
    sccs = kosaraju_scc(graph)
    assert len(sccs) == 5
    assert all(len(scc) == 1 for scc in sccs)

def test_single_node_graph():
    # Single node graph
    graph = {1: []}
    sccs = kosaraju_scc(graph)
    assert len(sccs) == 1
    assert sccs[0] == [1]

def test_disconnected_graph():
    # Disconnected graph with multiple SCCs
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    sccs = kosaraju_scc(graph)
    assert len(sccs) == 3
    assert sorted([sorted(scc) for scc in sccs]) == [[1, 2], [3, 4], [5]]

def test_empty_graph_raises_error():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        kosaraju_scc({})

def test_complete_graph():
    # Complete graph where every node is connected to every other node
    graph = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [1, 2, 3]
    }
    sccs = kosaraju_scc(graph)
    assert len(sccs) == 1
    assert sorted(sccs[0]) == [1, 2, 3, 4]
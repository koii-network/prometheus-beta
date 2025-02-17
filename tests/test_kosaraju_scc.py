import pytest
from src.kosaraju_scc import kosaraju_strongly_connected_components

def test_basic_scc():
    # Simple graph with two strongly connected components
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4]
    }
    
    sccs = kosaraju_strongly_connected_components(graph)
    assert len(sccs) == 2
    assert sorted([tuple(sorted(scc)) for scc in sccs]) == sorted([
        (1, 2, 3), 
        (4, 5, 6)
    ])

def test_single_component():
    # Graph with a single strongly connected component
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    
    sccs = kosaraju_strongly_connected_components(graph)
    assert len(sccs) == 1
    assert sorted(sccs[0]) == [1, 2, 3]

def test_disconnected_graph():
    # Completely disconnected graph
    graph = {
        1: [],
        2: [],
        3: []
    }
    
    sccs = kosaraju_strongly_connected_components(graph)
    assert len(sccs) == 3
    assert all(len(scc) == 1 for scc in sccs)

def test_empty_graph():
    # Empty graph
    graph = {}
    
    sccs = kosaraju_strongly_connected_components(graph)
    assert len(sccs) == 0

def test_complex_graph():
    # More complex graph with multiple SCCs
    graph = {
        1: [2],
        2: [3],
        3: [1, 4],
        4: [5],
        5: [6],
        6: [4, 7],
        7: []
    }
    
    sccs = kosaraju_strongly_connected_components(graph)
    assert len(sccs) == 3
    
    scc_sets = [set(scc) for scc in sccs]
    assert any(set(scc) == {1, 2, 3} for scc in scc_sets)
    assert any(set(scc) == {4, 5, 6} for scc in scc_sets)
    assert any(set(scc) == {7} for scc in scc_sets)

def test_graph_with_self_loop():
    # Graph with self-loops
    graph = {
        1: [1, 2],
        2: [3],
        3: [1]
    }
    
    sccs = kosaraju_strongly_connected_components(graph)
    assert len(sccs) == 1
    assert sorted(sccs[0]) == [1, 2, 3]
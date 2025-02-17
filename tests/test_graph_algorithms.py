import pytest
from src.graph_algorithms import kosaraju_scc

def test_kosaraju_basic_scc():
    """Test basic strongly connected component scenario"""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4]
    }
    
    sccs = kosaraju_scc(graph)
    
    # Check number of components and their contents
    assert len(sccs) == 2
    assert set(map(tuple, sccs)) == {(1, 2, 3), (4, 5, 6)}

def test_kosaraju_single_component():
    """Test graph with a single strongly connected component"""
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    
    sccs = kosaraju_scc(graph)
    
    assert len(sccs) == 1
    assert sorted(sccs[0]) == [1, 2, 3]

def test_kosaraju_disconnected_graph():
    """Test graph with disconnected components"""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    
    sccs = kosaraju_scc(graph)
    
    assert len(sccs) == 3
    assert set(map(tuple, sccs)) == {(1, 2), (3, 4), (5,)}

def test_kosaraju_empty_graph():
    """Test error handling for empty graph"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        kosaraju_scc({})

def test_kosaraju_graph_with_no_cycles():
    """Test graph with no strongly connected components"""
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [5]
    }
    
    sccs = kosaraju_scc(graph)
    
    assert len(sccs) == 5
    assert all(len(component) == 1 for component in sccs)

def test_kosaraju_graph_with_self_loops():
    """Test graph with self-loops"""
    graph = {
        1: [1, 2],
        2: [3],
        3: [1]
    }
    
    sccs = kosaraju_scc(graph)
    
    assert len(sccs) == 1
    assert sorted(sccs[0]) == [1, 2, 3]
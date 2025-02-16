import pytest
from src.prims_algorithm import prims_algorithm

def test_prims_algorithm_basic_graph():
    # Basic graph with multiple nodes and weighted edges
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (8, 2), (5, 4)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(2, 4), (3, 14), (4, 10), (6, 2)],
        6: [(5, 2), (7, 1), (8, 6)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)]
    }
    
    mst = prims_algorithm(graph)
    
    # Check that the number of edges is correct (n-1 edges for n nodes)
    assert len(mst) == len(graph) - 1
    
    # Verify the total weight of the MST
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 37

def test_prims_algorithm_single_node_graph():
    # Single node graph
    graph = {0: []}
    
    mst = prims_algorithm(graph)
    assert len(mst) == 0

def test_prims_algorithm_two_node_graph():
    # Two node graph
    graph = {
        0: [(1, 5)],
        1: [(0, 5)]
    }
    
    mst = prims_algorithm(graph)
    assert len(mst) == 1
    assert mst[0][2] == 5

def test_prims_algorithm_empty_graph():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_algorithm({})

def test_prims_algorithm_disconnected_graph():
    # Disconnected graph should raise ValueError
    graph = {
        0: [(1, 1)],
        1: [(0, 1)],
        2: [(3, 1)],
        3: [(2, 1)]
    }
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        prims_algorithm(graph)
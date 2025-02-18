import pytest
from src.prims_algorithm import prims_algorithm

def test_prims_algorithm_simple_graph():
    # Simple connected graph
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    
    mst = prims_algorithm(graph)
    
    # Check the number of edges in MST
    assert len(mst) == len(graph) - 1
    
    # Verify total weight (sum of edge weights)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 16  # Known minimum spanning tree weight for this graph

def test_prims_algorithm_single_vertex_graph():
    # Graph with a single vertex
    graph = {'A': {}}
    
    mst = prims_algorithm(graph)
    
    # MST of a single vertex should be an empty list of edges
    assert len(mst) == 0

def test_prims_algorithm_empty_graph():
    # Empty graph should raise a ValueError
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_algorithm({})

def test_prims_algorithm_disconnected_graph():
    # Disconnected graph should raise a ValueError
    graph = {
        'A': {'B': 1},
        'C': {'D': 2}
    }
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        prims_algorithm(graph)

def test_prims_algorithm_vertex_order_invariance():
    # Test that the algorithm works regardless of vertex order
    graph1 = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }
    
    graph2 = {
        'C': {'A': 2, 'B': 1, 'D': 8},
        'A': {'B': 4, 'C': 2},
        'D': {'B': 5, 'C': 8},
        'B': {'A': 4, 'C': 1, 'D': 5}
    }
    
    mst1 = prims_algorithm(graph1)
    mst2 = prims_algorithm(graph2)
    
    # Compare the sets of edges (ignoring the order)
    assert set(tuple(sorted(edge)) for edge in mst1) == set(tuple(sorted(edge)) for edge in mst2)
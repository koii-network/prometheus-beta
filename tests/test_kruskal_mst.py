import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet basic operations"""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # After union, vertices should be in the same set
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Second union should return False if already in same set
    assert not ds.union(0, 1)

def test_kruskal_simple_graph():
    """Test Kruskal's algorithm on a simple graph"""
    # Graph: [(weight, u, v), ...]
    graph = [
        (1, 0, 1),
        (3, 1, 2),
        (4, 0, 2),
        (5, 1, 3),
        (6, 2, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST edges (total weight 4)
    expected_mst = [(1, 0, 1), (3, 1, 2)]
    
    # Check MST size and edges
    assert len(mst) == 2
    assert sorted(mst) == sorted(expected_mst)

def test_kruskal_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph"""
    graph = [
        (1, 0, 1),
        (2, 2, 3),
        (3, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Minimum edges to connect vertices
    assert len(mst) == 2

def test_kruskal_empty_graph():
    """Test Kruskal's algorithm with empty graph"""
    with pytest.raises(ValueError):
        kruskal_mst([])

def test_kruskal_single_vertex():
    """Test Kruskal's algorithm with single vertex"""
    graph = [(1, 0, 0)]
    mst = kruskal_mst(graph)
    assert len(mst) == 0  # No edges in MST for single vertex graph

def test_kruskal_all_edges_in_mst():
    """Test a scenario where all edges are part of MST"""
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected number of vertices is number of vertices - 1
    # All edges should form a tree
    assert len(mst) == 2
    
    # Sum of all weights in MST
    mst_weight = sum(edge[0] for edge in mst)
    assert mst_weight == 3

def test_kruskal_graph_with_duplicate_weights():
    """Test Kruskal's algorithm with duplicate edge weights"""
    graph = [
        (1, 0, 1),
        (1, 1, 2),
        (2, 0, 2),
        (3, 1, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # MST with minimal weight and no cycles
    assert len(mst) == 2
    assert sum(edge[0] for edge in mst) <= 3
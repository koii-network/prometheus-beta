import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_initialization():
    """Test DisjointSet initialization."""
    ds = DisjointSet(5)
    assert ds.parent == [0, 1, 2, 3, 4]
    assert ds.rank == [0, 0, 0, 0, 0]

def test_disjoint_set_find():
    """Test find method of DisjointSet."""
    ds = DisjointSet(5)
    for i in range(5):
        assert ds.find(i) == i

def test_disjoint_set_union():
    """Test union method of DisjointSet."""
    ds = DisjointSet(5)
    assert ds.union(0, 1) == True  # First union should succeed
    assert ds.find(0) == ds.find(1)  # Should be in same set
    assert ds.union(0, 1) == False  # Subsequent union should fail

def test_kruskal_mst_basic():
    """Test Kruskal's algorithm with a simple graph."""
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    expected_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
    result = kruskal_mst(vertices, edges)
    
    assert len(result) == vertices - 1
    assert sorted(result) == sorted(expected_mst)

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with empty graph."""
    vertices = 0
    edges = []
    
    result = kruskal_mst(vertices, edges)
    assert result == []

def test_kruskal_mst_single_vertex():
    """Test Kruskal's algorithm with single vertex."""
    vertices = 1
    edges = []
    
    result = kruskal_mst(vertices, edges)
    assert result == []

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph."""
    vertices = 5
    edges = [
        (0, 1, 1),
        (2, 3, 2),
        (3, 4, 3)
    ]
    
    result = kruskal_mst(vertices, edges)
    assert len(result) == 3  # Will connect all available edges possible

def test_invalid_vertex_count():
    """Test error handling for negative vertex count."""
    with pytest.raises(ValueError):
        kruskal_mst(-1, [])
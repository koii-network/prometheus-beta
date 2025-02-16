import pytest
from src.boruvka_mst import boruvka_mst

def test_basic_mst():
    """Test a simple graph with known minimum spanning tree."""
    edges = [
        (4, 0, 1),
        (8, 1, 2),
        (7, 2, 3),
        (9, 3, 4),
        (10, 4, 0),
        (2, 0, 2),
        (1, 1, 3)
    ]
    num_vertices = 5
    
    mst = boruvka_mst(num_vertices, edges)
    
    # Expected MST edges (sorted)
    expected_mst = [(1, 1, 3), (2, 0, 2), (4, 0, 1), (9, 3, 4)]
    
    # Sort both to compare
    mst_sorted = sorted(mst)
    expected_mst_sorted = sorted(expected_mst)
    
    assert mst_sorted == expected_mst_sorted

def test_empty_graph():
    """Test with no edges."""
    edges = []
    num_vertices = 3
    
    mst = boruvka_mst(num_vertices, edges)
    
    assert mst == []

def test_single_vertex():
    """Test with a single vertex."""
    edges = []
    num_vertices = 1
    
    mst = boruvka_mst(num_vertices, edges)
    
    assert mst == []

def test_invalid_vertices():
    """Test with invalid number of vertices."""
    edges = [(1, 0, 1)]
    
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(0, edges)
    
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(-1, edges)

def test_disconnected_graph():
    """Test a graph with multiple disconnected components."""
    edges = [
        (1, 0, 1),   # Component 1
        (2, 2, 3),   # Component 2 
    ]
    num_vertices = 4
    
    mst = boruvka_mst(num_vertices, edges)
    
    # The MST should be empty as graph is not fully connected
    assert mst == []
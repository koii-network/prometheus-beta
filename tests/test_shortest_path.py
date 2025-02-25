import pytest
from src.shortest_path import Node, find_shortest_path

def test_simple_path():
    """Test finding a simple path between two nodes"""
    nodes = [
        Node('A', 'start'), 
        Node('B', 'intermediate'), 
        Node('C', 'end')
    ]
    edges = [
        ('A', 'B', 5),
        ('B', 'C', 3)
    ]
    
    path = find_shortest_path(nodes, edges, 'A', 'C')
    assert path == ['A', 'B', 'C']

def test_multiple_paths():
    """Test finding the shortest path when multiple paths exist"""
    nodes = [
        Node('A', 'start'), 
        Node('B', 'intermediate'), 
        Node('C', 'intermediate'), 
        Node('D', 'end')
    ]
    edges = [
        ('A', 'B', 5),
        ('A', 'C', 2),
        ('B', 'D', 3),
        ('C', 'D', 1)
    ]
    
    path = find_shortest_path(nodes, edges, 'A', 'D')
    assert path == ['A', 'C', 'D']

def test_no_path():
    """Test when no path exists between nodes"""
    nodes = [
        Node('A', 'start'), 
        Node('B', 'intermediate'), 
        Node('C', 'end')
    ]
    edges = [
        ('A', 'B', 5)
    ]
    
    path = find_shortest_path(nodes, edges, 'A', 'C')
    assert path is None

def test_nonexistent_nodes():
    """Test with nonexistent source or target nodes"""
    nodes = [
        Node('A', 'start'), 
        Node('B', 'end')
    ]
    edges = [
        ('A', 'B', 5)
    ]
    
    # Nonexistent source node
    path = find_shortest_path(nodes, edges, 'C', 'B')
    assert path is None
    
    # Nonexistent target node
    path = find_shortest_path(nodes, edges, 'A', 'C')
    assert path is None

def test_single_node():
    """Test finding path to the same node"""
    nodes = [
        Node('A', 'single')
    ]
    edges = []
    
    path = find_shortest_path(nodes, edges, 'A', 'A')
    assert path == ['A']
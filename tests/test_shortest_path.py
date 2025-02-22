import pytest
from src.shortest_path import Node, find_shortest_path

def test_basic_shortest_path():
    # Create nodes
    nodes = [
        Node('A', 'city'),
        Node('B', 'city'),
        Node('C', 'city')
    ]
    
    # Create edges with weights
    edges = [
        (nodes[0], nodes[1], 1.0),  # A -> B (weight 1)
        (nodes[1], nodes[2], 2.0),  # B -> C (weight 2)
        (nodes[0], nodes[2], 4.0)   # A -> C (weight 4, less efficient)
    ]
    
    # Expected path: A -> B -> C
    path = find_shortest_path(nodes, edges)
    
    assert path is not None
    assert len(path) == 3
    assert path[0].id == 'A'
    assert path[1].id == 'B'
    assert path[2].id == 'C'

def test_single_node():
    # Test with only one node
    nodes = [Node('A', 'city')]
    edges = []
    
    path = find_shortest_path(nodes, edges)
    assert path is None

def test_no_path():
    # Create nodes with no connecting path
    nodes = [
        Node('A', 'city'),
        Node('B', 'city')
    ]
    
    edges = [
        (nodes[1], nodes[0], 1.0)  # Path is reversed
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path is None

def test_multiple_node_types():
    # Create nodes with different types
    nodes = [
        Node('Start', 'origin'),
        Node('Midpoint', 'waypoint'),
        Node('End', 'destination')
    ]
    
    edges = [
        (nodes[0], nodes[1], 1.5),
        (nodes[1], nodes[2], 2.5)
    ]
    
    path = find_shortest_path(nodes, edges)
    
    assert path is not None
    assert len(path) == 3
    assert path[0].id == 'Start'
    assert path[1].id == 'Midpoint'
    assert path[2].id == 'End'

def test_complex_graph():
    # Create a more complex graph with multiple possible paths
    nodes = [
        Node('A', 'start'),
        Node('B', 'intermediate'),
        Node('C', 'intermediate'),
        Node('D', 'end')
    ]
    
    edges = [
        (nodes[0], nodes[1], 1.0),   # A -> B (weight 1)
        (nodes[0], nodes[2], 3.0),   # A -> C (weight 3)
        (nodes[1], nodes[3], 2.0),   # B -> D (weight 2)
        (nodes[2], nodes[3], 1.0)    # C -> D (weight 1)
    ]
    
    path = find_shortest_path(nodes, edges)
    
    assert path is not None
    assert len(path) == 3
    assert path[0].id == 'A'
    assert path[1].id == 'B'
    assert path[2].id == 'D'
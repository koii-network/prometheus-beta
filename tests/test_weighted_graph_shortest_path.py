import pytest
from src.weighted_graph_shortest_path import Node, find_shortest_path

def test_basic_path():
    """Test a simple path between two nodes"""
    nodes = [
        Node(1, 'start'), 
        Node(2, 'intermediate'), 
        Node(3, 'end')
    ]
    edges = [
        (nodes[0], nodes[1], 2.0),
        (nodes[1], nodes[2], 3.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert len(path) == 3
    assert path[0] == nodes[0]
    assert path[1] == nodes[1]
    assert path[2] == nodes[2]

def test_multiple_paths():
    """Test scenario with multiple possible paths"""
    nodes = [
        Node(1, 'start'), 
        Node(2, 'intermediate1'), 
        Node(3, 'intermediate2'), 
        Node(4, 'end')
    ]
    edges = [
        (nodes[0], nodes[1], 2.0),
        (nodes[0], nodes[2], 1.0),
        (nodes[1], nodes[3], 3.0),
        (nodes[2], nodes[3], 2.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert len(path) == 3
    assert path[0] == nodes[0]
    assert path[1] == nodes[2]
    assert path[2] == nodes[3]

def test_no_path():
    """Test scenario with no path between nodes"""
    nodes = [
        Node(1, 'start'), 
        Node(2, 'isolated'), 
        Node(3, 'end')
    ]
    edges = [
        (nodes[0], nodes[1], 2.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert len(path) == 0

def test_single_node():
    """Test scenario with a single node"""
    nodes = [Node(1, 'single')]
    edges = []
    
    path = find_shortest_path(nodes, edges)
    assert len(path) == 1
    assert path[0] == nodes[0]

def test_empty_nodes():
    """Test error handling for empty nodes list"""
    with pytest.raises(ValueError):
        find_shortest_path([], [])

def test_node_type_handling():
    """Test that node types are considered in node comparison"""
    nodes = [
        Node(1, 'start'), 
        Node(1, 'different'), 
        Node(2, 'end')
    ]
    edges = [
        (nodes[0], nodes[2], 2.0),
        (nodes[1], nodes[2], 3.0)
    ]
    
    path = find_shortest_path(nodes, edges)
    assert path[0] == nodes[0]
    assert path[-1] == nodes[2]
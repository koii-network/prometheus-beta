import pytest
from src.multi_type_graph_shortest_path import Node, find_shortest_path

def test_basic_shortest_path():
    # Create nodes
    node_a = Node('A', 'start')
    node_b = Node('B', 'intermediate')
    node_c = Node('C', 'target')
    
    # Create edges
    edges = [
        (node_a, node_b, 2.0),
        (node_b, node_c, 3.0),
        (node_a, node_c, 6.0)
    ]
    
    # Find shortest path
    path = find_shortest_path([node_a, node_b, node_c], edges)
    
    # Assert path is correct
    assert len(path) == 3
    assert path[0] == node_a
    assert path[1] == node_b
    assert path[2] == node_c

def test_direct_path():
    # Create nodes
    node_a = Node('A', 'start')
    node_b = Node('B', 'target')
    
    # Create edges
    edges = [
        (node_a, node_b, 5.0)
    ]
    
    # Find shortest path
    path = find_shortest_path([node_a, node_b], edges)
    
    # Assert path is correct
    assert len(path) == 2
    assert path[0] == node_a
    assert path[1] == node_b

def test_no_path():
    # Create nodes with no connecting edges
    node_a = Node('A', 'start')
    node_b = Node('B', 'target')
    
    # Empty edges list
    edges = []
    
    # Find shortest path
    path = find_shortest_path([node_a, node_b], edges)
    
    # Assert empty path
    assert len(path) == 0

def test_multiple_paths():
    # Create nodes
    node_a = Node('A', 'start')
    node_b = Node('B', 'intermediate1')
    node_c = Node('C', 'intermediate2')
    node_d = Node('D', 'target')
    
    # Create edges with multiple possible paths
    edges = [
        (node_a, node_b, 2.0),
        (node_b, node_d, 3.0),
        (node_a, node_c, 1.0),
        (node_c, node_d, 2.0)
    ]
    
    # Find shortest path
    path = find_shortest_path([node_a, node_b, node_c, node_d], edges)
    
    # Assert path is the shorter route
    assert len(path) == 3
    assert path[0] == node_a
    assert path[1] == node_c
    assert path[2] == node_d

def test_empty_nodes_list():
    # Test empty nodes list
    with pytest.raises(ValueError):
        find_shortest_path([], [])
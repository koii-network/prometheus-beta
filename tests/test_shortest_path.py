import pytest
from src.shortest_path import Node, find_shortest_path

def test_basic_shortest_path():
    # Create nodes
    node_a = Node('A', 'city')
    node_b = Node('B', 'city')
    node_c = Node('C', 'city')
    
    # Create edges (from_node, to_node, weight)
    edges = [
        (node_a, node_b, 1.0),
        (node_b, node_c, 2.0),
        (node_a, node_c, 4.0)
    ]
    
    # Define nodes list in order (start to end)
    nodes = [node_a, node_b, node_c]
    
    # Find shortest path
    path = find_shortest_path(nodes, edges)
    
    # Assert path
    assert len(path) == 3
    assert path[0] == node_a
    assert path[1] == node_b
    assert path[2] == node_c

def test_different_node_types():
    # Create nodes with different types
    node_a = Node('A', 'start')
    node_b = Node('B', 'intermediate')
    node_c = Node('C', 'end')
    
    # Create edges
    edges = [
        (node_a, node_b, 1.5),
        (node_b, node_c, 2.5),
        (node_a, node_c, 5.0)
    ]
    
    # Define nodes list in order
    nodes = [node_a, node_b, node_c]
    
    # Find shortest path
    path = find_shortest_path(nodes, edges)
    
    # Assert path
    assert len(path) == 3
    assert path[0] == node_a
    assert path[1] == node_b
    assert path[2] == node_c

def test_no_path_raises_error():
    # Create nodes
    node_a = Node('A', 'city')
    node_b = Node('B', 'city')
    
    # No edges connecting them
    edges = []
    
    # Define nodes list in order
    nodes = [node_a, node_b]
    
    # Expect ValueError
    with pytest.raises(ValueError, match="No path exists"):
        find_shortest_path(nodes, edges)

def test_insufficient_nodes():
    # Single node
    node_a = Node('A', 'city')
    
    # Expect ValueError
    with pytest.raises(ValueError, match="At least two nodes are required"):
        find_shortest_path([node_a], [])
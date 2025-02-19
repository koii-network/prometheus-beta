import pytest
from src.multi_type_shortest_path import Node, find_shortest_path

def test_basic_path():
    # Create nodes
    n1 = Node('A', 'start')
    n2 = Node('B', 'intermediate')
    n3 = Node('C', 'end')
    
    # Create edges
    edges = [
        (n1, n2, 2.0),  # A -> B with weight 2
        (n2, n3, 3.0),  # B -> C with weight 3
    ]
    
    # Get shortest path
    path = find_shortest_path([n1, n2, n3], edges)
    
    # Check path
    assert len(path) == 3
    assert path[0] == n1
    assert path[1] == n2
    assert path[2] == n3

def test_multiple_paths():
    # Create nodes with multiple possible paths
    n1 = Node('A', 'start')
    n2 = Node('B', 'intermediate1')
    n3 = Node('C', 'intermediate2')
    n4 = Node('D', 'end')
    
    # Create edges with multiple paths
    edges = [
        (n1, n2, 2.0),  # A -> B with weight 2
        (n1, n3, 5.0),  # A -> C with weight 5
        (n2, n4, 3.0),  # B -> D with weight 3
        (n3, n4, 1.0),  # C -> D with weight 1
    ]
    
    # Get shortest path
    path = find_shortest_path([n1, n2, n3, n4], edges)
    
    # Check path
    assert len(path) == 3
    assert path[0] == n1
    assert path[1] == n3
    assert path[2] == n4

def test_same_node_start_end():
    # Create a single node
    n1 = Node('A', 'single')
    
    # Get shortest path
    path = find_shortest_path([n1], [])
    
    # Check path
    assert len(path) == 1
    assert path[0] == n1

def test_no_path_raises_error():
    # Create disconnected nodes
    n1 = Node('A', 'start')
    n2 = Node('B', 'end')
    
    # No edges connecting the nodes
    edges = []
    
    # Expect ValueError
    with pytest.raises(ValueError, match="No path exists"):
        find_shortest_path([n1, n2], edges)

def test_empty_nodes_raises_error():
    # Empty nodes list
    nodes = []
    edges = []
    
    # Expect ValueError
    with pytest.raises(ValueError, match="No nodes provided"):
        find_shortest_path(nodes, edges)
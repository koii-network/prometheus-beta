import pytest
from src.shortest_path import Node, find_shortest_path

def test_basic_shortest_path():
    nodes = [
        Node('A', 'start'),
        Node('B', 'intermediate'),
        Node('C', 'end')
    ]
    edges = [
        (nodes[0], nodes[1], 2.0),
        (nodes[1], nodes[2], 3.0)
    ]
    path = find_shortest_path(nodes, edges)
    
    assert len(path) == 3
    assert [node.name for node in path] == ['A', 'B', 'C']

def test_multiple_paths():
    nodes = [
        Node('A', 'start'),
        Node('B', 'intermediate1'),
        Node('C', 'intermediate2'),
        Node('D', 'end')
    ]
    edges = [
        (nodes[0], nodes[1], 1.0),
        (nodes[1], nodes[3], 5.0),
        (nodes[0], nodes[2], 2.0),
        (nodes[2], nodes[3], 2.0)
    ]
    path = find_shortest_path(nodes, edges)
    
    assert len(path) == 3
    assert [node.name for node in path] == ['A', 'C', 'D']

def test_no_path():
    nodes = [
        Node('A', 'start'),
        Node('B', 'intermediate'),
        Node('C', 'end')
    ]
    edges = [
        (nodes[1], nodes[2], 3.0)  # No path from A to C
    ]
    path = find_shortest_path(nodes, edges)
    
    assert len(path) == 0

def test_single_node():
    nodes = [Node('A', 'single')]
    edges = []
    path = find_shortest_path(nodes, edges)
    
    assert len(path) == 1
    assert path[0].name == 'A'

def test_empty_graph():
    nodes = []
    edges = []
    path = find_shortest_path(nodes, edges)
    
    assert len(path) == 0
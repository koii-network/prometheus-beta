import pytest
from src.bfs import breadth_first_search

def test_basic_bfs():
    # Simple graph with integer nodes
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []
    }
    
    # BFS starting from node 1
    result = breadth_first_search(graph, 1)
    assert result == [1, 2, 3, 4, 5, 6], "Basic BFS traversal should visit nodes in correct order"

def test_disconnected_graph():
    # Graph with some disconnected nodes
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': [],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # BFS starting from 'A'
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D'], "BFS should handle different node types and disconnected nodes"

def test_single_node_graph():
    # Graph with only one node
    graph = {
        'X': []
    }
    
    # BFS starting from the only node
    result = breadth_first_search(graph, 'X')
    assert result == ['X'], "BFS on a single node graph should return that node"

def test_start_node_not_in_graph():
    graph = {
        1: [2, 3],
        2: [4],
        3: []
    }
    
    # Try BFS with a non-existent start node
    with pytest.raises(ValueError, match="Start node 4 not found in the graph"):
        breadth_first_search(graph, 4)

def test_cyclic_graph():
    # Graph with a cycle
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    
    # BFS starting from 'A'
    result = breadth_first_search(graph, 'A')
    assert set(result) == {'A', 'B', 'C', 'D'}, "BFS should handle cyclic graphs without infinite loops"
    assert result[0] == 'A', "First node should be the start node"
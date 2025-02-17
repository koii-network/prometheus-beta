import pytest
from src.shortest_path_bfs import shortest_path_bfs

def test_shortest_path_basic():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Test direct path
    assert shortest_path_bfs(graph, 'A', 'B') == ['A', 'B']
    
    # Test multi-hop path
    result = shortest_path_bfs(graph, 'A', 'F')
    assert result == ['A', 'C', 'F'] or result == ['A', 'B', 'E', 'F']

def test_shortest_path_numeric_nodes():
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    
    # Test direct path
    assert shortest_path_bfs(graph, 1, 2) == [1, 2]
    
    # Test multi-hop path
    result = shortest_path_bfs(graph, 1, 6)
    assert result == [1, 3, 6] or result == [1, 2, 5, 6]

def test_no_path_between_nodes():
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    # No path between disconnected components
    assert shortest_path_bfs(graph, 'A', 'C') is None

def test_start_or_end_not_in_graph():
    graph = {'A': ['B'], 'B': ['A']}
    
    # Start or end node not in graph
    assert shortest_path_bfs(graph, 'C', 'A') is None
    assert shortest_path_bfs(graph, 'A', 'C') is None

def test_single_node_graph():
    graph = {'A': []}
    
    # Path from a node to itself
    assert shortest_path_bfs(graph, 'A', 'A') == ['A']
    
    # No path to non-existent node
    assert shortest_path_bfs(graph, 'A', 'B') is None
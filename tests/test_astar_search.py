import pytest
from src.astar_search import astar_search
import math

def test_simple_path_finding():
    """
    Test A* search on a simple grid-like scenario
    """
    # Create a simple grid representation
    grid = {
        (0, 0): [(1, 0), (0, 1)],
        (1, 0): [(0, 0), (1, 1)],
        (0, 1): [(0, 0), (1, 1)],
        (1, 1): [(1, 0), (0, 1), (2, 1)],
        (2, 1): [(1, 1)]
    }
    
    def get_neighbors(node):
        return [(neighbor, 1) for neighbor in grid.get(node, [])]
    
    def heuristic(node):
        # Manhattan distance heuristic
        return abs(node[0] - 2) + abs(node[1] - 1)
    
    def is_goal(node):
        return node == (2, 1)
    
    path = astar_search((0, 0), is_goal, get_neighbors, heuristic)
    
    assert path == [(0, 0), (1, 0), (1, 1), (2, 1)]

def test_no_path():
    """
    Test scenario where no path exists
    """
    def get_neighbors(node):
        return []
    
    def heuristic(node):
        return 0
    
    def is_goal(node):
        return False
    
    path = astar_search(1, is_goal, get_neighbors, heuristic)
    
    assert path == []

def test_start_is_goal():
    """
    Test when start node is the goal
    """
    def get_neighbors(node):
        return []
    
    def heuristic(node):
        return 0
    
    def is_goal(node):
        return node == 1
    
    path = astar_search(1, is_goal, get_neighbors, heuristic)
    
    assert path == [1]

def test_complex_path_finding():
    """
    Test A* search with a more complex graph
    """
    # Graph with weighted edges
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
        'E': [('C', 10), ('D', 2), ('F', 3)],
        'F': [('D', 6), ('E', 3)]
    }
    
    def get_neighbors(node):
        return graph.get(node, [])
    
    def heuristic(node):
        # Simple admissible heuristic 
        goal_distances = {'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 2, 'F': 0}
        return goal_distances.get(node, 0)
    
    def is_goal(node):
        return node == 'F'
    
    path = astar_search('A', is_goal, get_neighbors, heuristic)
    
    assert path == ['A', 'C', 'B', 'D', 'E', 'F']
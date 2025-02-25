import pytest
import math
from src.astar_search import astar_search

def test_grid_navigation():
    """
    Test A* search on a simple grid navigation problem.
    """
    # Grid where 0 is passable, 1 is obstacle
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    
    def get_neighbors(state):
        """Generate possible moves in the grid."""
        x, y = state
        neighbors = []
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            # Check if move is within grid and not an obstacle
            if (0 <= new_x < len(grid) and 
                0 <= new_y < len(grid[0]) and 
                grid[new_x][new_y] == 0):
                neighbors.append(((new_x, new_y), 1))  # uniform cost
        
        return neighbors
    
    def heuristic(state):
        """Manhattan distance heuristic."""
        return abs(state[0] - 3) + abs(state[1] - 3)
    
    def is_goal(state):
        """Check if reached bottom-right corner."""
        return state == (3, 3)
    
    # Find path from top-left to bottom-right
    path = astar_search((0,0), is_goal, get_neighbors, heuristic)
    
    assert path is not None, "Path should exist"
    assert path[0] == (0,0), "Path should start at start state"
    assert path[-1] == (3,3), "Path should end at goal state"
    assert len(path) > 0, "Path should have at least one step"

def test_no_path_exists():
    """
    Test scenario where no path exists.
    """
    # Grid with no possible path
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    
    def get_neighbors(state):
        """Generate possible moves in the grid."""
        x, y = state
        neighbors = []
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            # Check if move is within grid and not an obstacle
            if (0 <= new_x < len(grid) and 
                0 <= new_y < len(grid[0]) and 
                grid[new_x][new_y] == 0):
                neighbors.append(((new_x, new_y), 1))  # uniform cost
        
        return neighbors
    
    def heuristic(state):
        """Manhattan distance heuristic."""
        return abs(state[0] - 2) + abs(state[1] - 2)
    
    def is_goal(state):
        """Check if reached bottom-right corner."""
        return state == (2, 2)
    
    # Attempt to find path from top-left to bottom-right
    path = astar_search((0,0), is_goal, get_neighbors, heuristic)
    
    assert path is None, "Path should not exist when blocked"

def test_start_is_goal():
    """
    Test when start state is already the goal state.
    """
    def get_neighbors(state):
        return []  # No neighbors
    
    def heuristic(state):
        return 0
    
    def is_goal(state):
        return state == 'goal'
    
    path = astar_search('goal', is_goal, get_neighbors, heuristic)
    
    assert path == ['goal'], "Path should be single state when start is goal"

def test_non_trivial_heuristic():
    """
    Test with a more complex heuristic and state space.
    """
    # Simulate a weighted graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 3)],
        'C': [('D', 1)],
        'D': [('E', 2)],
        'E': []
    }
    
    def get_neighbors(state):
        """Get neighbors from the graph."""
        return graph.get(state, [])
    
    def heuristic(state):
        """
        Heuristic based on some predefined goal-oriented estimate.
        """
        h_values = {
            'A': 5,
            'B': 3,
            'C': 4,
            'D': 1,
            'E': 0
        }
        return h_values.get(state, float('inf'))
    
    def is_goal(state):
        return state == 'E'
    
    path = astar_search('A', is_goal, get_neighbors, heuristic)
    
    assert path is not None, "Path should exist"
    assert path[0] == 'A', "Path should start at start state"
    assert path[-1] == 'E', "Path should end at goal state"
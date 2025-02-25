import pytest
import sys
import os

# Ensure src directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from astar_search import astar_search

def test_simple_path():
    """
    Test a simple path finding scenario
    """
    def is_goal(state):
        return state == 5
    
    def get_neighbors(state):
        return [(state + 1, 1), (state + 2, 2)]
    
    def heuristic(state):
        return abs(5 - state)
    
    path = astar_search(1, is_goal, get_neighbors, heuristic)
    assert path is not None
    assert path == [1, 3, 5]

def test_grid_navigation():
    """
    Test path finding in a grid-like environment
    """
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    
    def is_goal(state):
        return state == (3, 3)
    
    def get_neighbors(state):
        x, y = state
        neighbors = []
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < 4 and 0 <= new_y < 4 and grid[new_x][new_y] == 0):
                neighbors.append(((new_x, new_y), 1))
        return neighbors
    
    def heuristic(state):
        x, y = state
        return abs(3 - x) + abs(3 - y)
    
    path = astar_search((0, 0), is_goal, get_neighbors, heuristic)
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)

def test_no_path():
    """
    Test scenario where no path exists
    """
    def is_goal(state):
        return state == 5
    
    def get_neighbors(state):
        return []  # No neighbors
    
    def heuristic(state):
        return abs(5 - state)
    
    path = astar_search(1, is_goal, get_neighbors, heuristic)
    assert path is None

def test_invalid_input():
    """
    Test error handling for invalid inputs
    """
    with pytest.raises(ValueError):
        astar_search(1, None, None, None)

def test_single_step_path():
    """
    Test when start is the goal state
    """
    def is_goal(state):
        return state == 5
    
    def get_neighbors(state):
        return []
    
    def heuristic(state):
        return 0
    
    path = astar_search(5, is_goal, get_neighbors, heuristic)
    assert path == [5]
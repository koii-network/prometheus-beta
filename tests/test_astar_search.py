import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from astar_search import astar_search

def test_simple_path():
    """Test a simple path finding scenario."""
    def get_neighbors(state):
        x, y = state
        return [
            ((x+1, y), 1),
            ((x-1, y), 1),
            ((x, y+1), 1),
            ((x, y-1), 1)
        ]
    
    def heuristic(state):
        # Manhattan distance heuristic
        return abs(state[0] - 4) + abs(state[1] - 4)
    
    def is_goal(state):
        return state == (4, 4)
    
    path = astar_search((0, 0), is_goal, get_neighbors, heuristic)
    
    assert path is not None, "Path should exist"
    assert path[0] == (0, 0), "Path should start at initial state"
    assert path[-1] == (4, 4), "Path should end at goal state"
    assert len(path) == 9, "Path should have correct length"

def test_no_path():
    """Test scenario where no path exists."""
    def get_neighbors(state):
        # No valid neighbors
        return []
    
    def heuristic(state):
        return 0
    
    def is_goal(state):
        return False
    
    path = astar_search(1, is_goal, get_neighbors, heuristic)
    
    assert path is None, "Should return None when no path exists"

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        astar_search(None, None, None, None)
    
    def dummy_is_goal(state):
        return False
    
    with pytest.raises(ValueError):
        astar_search(1, dummy_is_goal, None, None)

def test_grid_path():
    """Test path finding in a more complex grid scenario."""
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    
    def get_neighbors(state):
        x, y = state
        neighbors = []
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < 5 and 0 <= new_y < 5 and 
                grid[new_y][new_x] == 0):
                neighbors.append(((new_x, new_y), 1))
        return neighbors
    
    def heuristic(state):
        # Manhattan distance
        return abs(state[0] - 4) + abs(state[1] - 4)
    
    def is_goal(state):
        return state == (4, 4)
    
    path = astar_search((0, 0), is_goal, get_neighbors, heuristic)
    
    assert path is not None, "Path should exist"
    assert path[0] == (0, 0), "Path should start at initial state"
    assert path[-1] == (4, 4), "Path should end at goal state"
    
    # Validate that path does not go through obstacles
    for x, y in path[1:-1]:
        assert grid[y][x] == 0, f"Path should not go through obstacles at {(x,y)}"

def test_single_node_path():
    """Test when start state is the goal state."""
    def get_neighbors(state):
        return []
    
    def heuristic(state):
        return 0
    
    def is_goal(state):
        return state == 1
    
    path = astar_search(1, is_goal, get_neighbors, heuristic)
    
    assert path == [1], "Should return single node when start is goal"
import pytest
from src.astar_search import astar_search

def test_simple_path():
    """Test finding a simple path in a grid-like environment."""
    def get_neighbors(state):
        x, y = state
        neighbors = [
            ((x+1, y), 1),   # Right
            ((x-1, y), 1),   # Left
            ((x, y+1), 1),   # Up
            ((x, y-1), 1)    # Down
        ]
        return neighbors

    def heuristic(state):
        # Manhattan distance heuristic
        goal = (4, 4)
        return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

    def is_goal(state):
        return state == (4, 4)

    path = astar_search((0, 0), is_goal, get_neighbors, heuristic)
    
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (4, 4)
    assert len(path) == 9  # Path from (0,0) to (4,4) should have 9 steps

def test_no_path():
    """Test scenario where no path exists."""
    def get_neighbors(state):
        return []  # No neighbors

    def heuristic(state):
        return 0

    def is_goal(state):
        return False

    path = astar_search(1, is_goal, get_neighbors, heuristic)
    
    assert path == []

def test_start_is_goal():
    """Test when start state is the goal state."""
    def get_neighbors(state):
        return []  # No neighbors needed

    def heuristic(state):
        return 0

    def is_goal(state):
        return state == 5

    path = astar_search(5, is_goal, get_neighbors, heuristic)
    
    assert path == [5]

def test_complex_neighbor_costs():
    """Test path finding with varying neighbor costs."""
    def get_neighbors(state):
        x = state
        return [
            (x+1, 2),   # Costly move to the right
            (x+2, 1),   # Cheaper move further right
            (x-1, 3)    # Costly move to the left
        ]

    def heuristic(state):
        return abs(state - 10)

    def is_goal(state):
        return state == 10

    path = astar_search(0, is_goal, get_neighbors, heuristic)
    
    assert path is not None
    assert path[0] == 0
    assert path[-1] == 10
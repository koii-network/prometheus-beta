import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from astar_search import astar_search

def test_simple_path():
    """
    Test a simple path finding scenario
    """
    # Graph-like problem where states are coordinates
    graph = {
        (0, 0): [((1, 0), 1), ((0, 1), 1)],
        (1, 0): [((0, 0), 1), ((1, 1), 1)],
        (0, 1): [((0, 0), 1), ((1, 1), 1)],
        (1, 1): [((1, 0), 1), ((0, 1), 1)]
    }
    
    def get_neighbors(state):
        return graph.get(state, [])
    
    def heuristic(state):
        # Manhattan distance to goal (1,1)
        return abs(state[0] - 1) + abs(state[1] - 1)
    
    result = astar_search(
        start=(0, 0),
        is_goal=lambda state: state == (1, 1),
        get_neighbors=get_neighbors,
        heuristic=heuristic
    )
    
    assert result is not None
    assert result == [(0, 0), (1, 0), (1, 1)] or result == [(0, 0), (0, 1), (1, 1)]

def test_no_path():
    """
    Test scenario where no path exists
    """
    graph = {
        (0, 0): [],  # No neighbors
    }
    
    def get_neighbors(state):
        return graph.get(state, [])
    
    def heuristic(state):
        return 0
    
    result = astar_search(
        start=(0, 0),
        is_goal=lambda state: state == (1, 1),
        get_neighbors=get_neighbors,
        heuristic=heuristic
    )
    
    assert result is None

def test_complex_path():
    """
    Test a more complex path finding scenario
    """
    graph = {
        (0, 0): [((1, 0), 1), ((0, 1), 2)],
        (1, 0): [((0, 0), 1), ((1, 1), 3), ((2, 0), 1)],
        (0, 1): [((0, 0), 2), ((1, 1), 1)],
        (1, 1): [((1, 0), 3), ((0, 1), 1), ((2, 1), 2)],
        (2, 0): [((1, 0), 1), ((2, 1), 1)],
        (2, 1): [((2, 0), 1), ((1, 1), 2)]
    }
    
    def get_neighbors(state):
        return graph.get(state, [])
    
    def heuristic(state):
        # Manhattan distance to goal (2,1)
        return abs(state[0] - 2) + abs(state[1] - 1)
    
    result = astar_search(
        start=(0, 0),
        is_goal=lambda state: state == (2, 1),
        get_neighbors=get_neighbors,
        heuristic=heuristic
    )
    
    assert result is not None
    # Validate the result reaches the goal
    assert result[-1] == (2, 1)

def test_start_is_goal():
    """
    Test when start state is the goal state
    """
    def get_neighbors(state):
        return []
    
    def heuristic(state):
        return 0
    
    result = astar_search(
        start=(1, 1),
        is_goal=lambda state: state == (1, 1),
        get_neighbors=get_neighbors,
        heuristic=heuristic
    )
    
    assert result == [(1, 1)]
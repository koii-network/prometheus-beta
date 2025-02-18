import pytest
from src.astar_search import astar_search

def test_simple_path_finding():
    """Test A* search for a simple grid-based path finding scenario."""
    def heuristic(state):
        # Manhattan distance heuristic
        return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    
    def get_successors(state):
        # 4-directional movement
        x, y = state
        possible_moves = [
            ((x+1, y), 1), ((x-1, y), 1),
            ((x, y+1), 1), ((x, y-1), 1)
        ]
        # Filter out obstacles or out-of-bounds moves
        return [
            move for move in possible_moves 
            if move[0] not in obstacles
        ]
    
    def goal_test(state):
        return state == goal
    
    start = (0, 0)
    goal = (4, 4)
    obstacles = {(1, 1), (2, 2), (3, 3)}
    
    path = astar_search(start, goal_test, get_successors, heuristic)
    
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) > 0

def test_no_path_exists():
    """Test scenario where no path exists."""
    def heuristic(state):
        return 0
    
    def get_successors(state):
        return []  # No possible moves
    
    def goal_test(state):
        return False  # Impossible goal
    
    start = "A"
    path = astar_search(start, goal_test, get_successors, heuristic)
    
    assert path == []

def test_start_is_goal():
    """Test when start state is the goal state."""
    def heuristic(state):
        return 0
    
    def get_successors(state):
        return []
    
    def goal_test(state):
        return state == "goal"
    
    start = "goal"
    path = astar_search(start, goal_test, get_successors, heuristic)
    
    assert path == ["goal"]

def test_graph_search():
    """Test A* search on a graph-like structure."""
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 3)],
        'C': [('D', 1)],
        'D': [('E', 2)],
        'E': []
    }
    
    def heuristic(state):
        # Placeholder heuristic
        return 0
    
    def get_successors(state):
        return graph.get(state, [])
    
    def goal_test(state):
        return state == 'E'
    
    path = astar_search('A', goal_test, get_successors, heuristic)
    
    assert path is not None
    assert path[0] == 'A'
    assert path[-1] == 'E'
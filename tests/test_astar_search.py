import pytest
from src.astar_search import astar_search

def test_astar_simple_grid():
    """Test A* search on a simple grid-based pathfinding scenario."""
    # Define a simple grid where 0 is passable, 1 is obstacle
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    
    def is_goal(pos):
        return pos == (3, 3)
    
    def get_neighbors(pos):
        x, y = pos
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        valid_neighbors = []
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(grid) and 
                0 <= new_y < len(grid[0]) and 
                grid[new_x][new_y] == 0):
                valid_neighbors.append(((new_x, new_y), 1))
        
        return valid_neighbors
    
    def heuristic(pos):
        # Manhattan distance to goal
        return abs(pos[0] - 3) + abs(pos[1] - 3)
    
    path = astar_search((0,0), is_goal, get_neighbors, heuristic)
    
    assert path is not None
    assert path[0] == (0,0)
    assert path[-1] == (3,3)
    assert len(path) > 0

def test_astar_no_path():
    """Test A* search when no path exists."""
    def is_goal(x):
        return x == 5
    
    def get_neighbors(x):
        return []
    
    def heuristic(x):
        return abs(x - 5)
    
    path = astar_search(0, is_goal, get_neighbors, heuristic)
    
    assert path == []

def test_astar_start_is_goal():
    """Test A* search when start node is the goal."""
    def is_goal(x):
        return x == 5
    
    def get_neighbors(x):
        return []
    
    def heuristic(x):
        return 0
    
    path = astar_search(5, is_goal, get_neighbors, heuristic)
    
    assert path == [5]

def test_astar_invalid_inputs():
    """Test A* search with invalid or edge case inputs."""
    with pytest.raises(TypeError):
        astar_search(None, None, None, None)
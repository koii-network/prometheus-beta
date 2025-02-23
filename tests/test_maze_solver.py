import pytest
from src.maze_solver import find_shortest_path, get_neighbors, is_valid

def test_get_neighbors():
    """Test get_neighbors returns correct neighboring cells."""
    assert set(get_neighbors((1, 1))) == {(0, 1), (2, 1), (1, 0), (1, 2)}

def test_is_valid():
    """Test is_valid correctly identifies valid and invalid cells."""
    maze = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 3]
    ]
    
    # Valid cells
    assert is_valid(maze, (0, 0)) == True
    assert is_valid(maze, (2, 2)) == True
    
    # Invalid cells (out of bounds or wall)
    assert is_valid(maze, (-1, 0)) == False
    assert is_valid(maze, (1, 1)) == False
    assert is_valid(maze, (3, 3)) == False

def test_find_shortest_path_basic():
    """Test finding a simple shortest path."""
    maze = [
        [0, 0, 0],
        [0, 1, 0],
        [2, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(2, 0), (2, 1), (2, 2)]

def test_find_shortest_path_multiple_routes():
    """Test finding the shortest path when multiple routes exist."""
    maze = [
        [2, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    # Verify the path is the shortest possible
    assert len(path) == 5
    assert path[0] == (0, 0)
    assert path[-1] == (2, 3)

def test_find_shortest_path_no_path():
    """Test when no path exists."""
    maze = [
        [2, 1, 0],
        [1, 1, 0],
        [0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_find_shortest_path_invalid_inputs():
    """Test error handling for invalid maze inputs."""
    with pytest.raises(ValueError, match="Maze cannot be empty"):
        find_shortest_path([])
    
    with pytest.raises(ValueError, match="Maze must have exactly one start"):
        find_shortest_path([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
    
    with pytest.raises(ValueError, match="Maze must have exactly one start"):
        find_shortest_path([
            [2, 2, 0],
            [0, 0, 0],
            [0, 0, 3]
        ])

def test_find_shortest_path_start_at_end():
    """Test when start and end are the same cell."""
    maze = [
        [0, 0, 0],
        [0, 2, 0],
        [0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(1, 1)]  # direct path to the end
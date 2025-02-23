import pytest
from src.maze_solver import find_shortest_path, get_neighbors, is_valid

def test_basic_maze_path():
    """Test finding a simple direct path"""
    maze = [
        [1, 1, 1, 1, 1],
        [1, 2, 0, 0, 1],
        [1, 0, 1, 3, 1],
        [1, 1, 1, 1, 1]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(1, 1), (1, 2), (1, 3), (2, 3)]

def test_maze_no_path():
    """Test maze with no possible path"""
    maze = [
        [1, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_maze_multiple_paths():
    """Test maze with multiple possible paths"""
    maze = [
        [1, 1, 1, 1, 1],
        [1, 2, 0, 0, 1],
        [1, 0, 0, 3, 1],
        [1, 1, 1, 1, 1]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    # Multiple valid paths, so just check start and end
    assert path[0] == (1, 1)
    assert path[-1] == (2, 3)

def test_empty_maze():
    """Test empty maze raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_no_start_or_end():
    """Test maze without start or end cell raises ValueError"""
    maze = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    with pytest.raises(ValueError):
        find_shortest_path(maze)

def test_neighbors():
    """Test get_neighbors function"""
    cell = (2, 3)
    neighbors = get_neighbors(cell)
    assert len(neighbors) == 4
    assert (1, 3) in neighbors
    assert (3, 3) in neighbors
    assert (2, 2) in neighbors
    assert (2, 4) in neighbors

def test_is_valid():
    """Test is_valid function"""
    maze = [
        [1, 1, 1],
        [1, 0, 3],
        [1, 1, 1]
    ]
    # Out of bounds
    assert not is_valid(maze, (-1, 0))
    assert not is_valid(maze, (3, 0))
    
    # Wall
    assert not is_valid(maze, (0, 0))
    
    # Empty or end cell
    assert is_valid(maze, (1, 1))  # Empty cell
    assert is_valid(maze, (1, 2))  # End cell
import pytest
from src.maze_shortest_path import find_shortest_path, get_neighbors, is_valid

def test_get_neighbors():
    """Test the get_neighbors function."""
    cell = (2, 3)
    expected_neighbors = [
        (1, 3),  # up
        (2, 4),  # right
        (3, 3),  # down
        (2, 2)   # left
    ]
    assert sorted(get_neighbors(cell)) == sorted(expected_neighbors)

def test_is_valid_within_bounds():
    """Test is_valid function for cells within maze bounds."""
    maze = [
        [0, 0, 0],
        [1, 1, 0],
        [2, 0, 3]
    ]
    
    assert is_valid(maze, (0, 0)) == True   # empty cell
    assert is_valid(maze, (2, 0)) == True   # start cell
    assert is_valid(maze, (2, 2)) == True   # end cell
    assert is_valid(maze, (1, 1)) == False  # wall
    assert is_valid(maze, (-1, 0)) == False  # out of bounds
    assert is_valid(maze, (3, 0)) == False  # out of bounds

def test_shortest_path_basic():
    """Test basic shortest path scenario."""
    maze = [
        [0, 0, 0],
        [1, 1, 0],
        [2, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(2, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

def test_shortest_path_no_path():
    """Test scenario with no possible path."""
    maze = [
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_shortest_path_start_at_end():
    """Test when start and end are the same cell."""
    maze = [
        [0, 0, 0],
        [0, 2, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path == [(1, 1)]

def test_multiple_path_options():
    """Test a maze with multiple possible paths."""
    maze = [
        [0, 0, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(1, 1), (2, 1), (2, 2), (2, 3)]

def test_missing_start_or_end():
    """Test raising an error when start or end is missing."""
    maze_no_start = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 3]
    ]
    
    maze_no_end = [
        [0, 0, 0],
        [1, 1, 0],
        [2, 0, 0]
    ]
    
    with pytest.raises(ValueError, match="Start or end cell not found in maze"):
        find_shortest_path(maze_no_start)
    
    with pytest.raises(ValueError, match="Start or end cell not found in maze"):
        find_shortest_path(maze_no_end)
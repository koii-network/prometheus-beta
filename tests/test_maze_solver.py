import pytest
from src.maze_solver import find_shortest_path

def test_simple_maze_path():
    """Test a simple maze with a direct path"""
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(1, 0), (1, 1), (1, 2)]

def test_maze_with_walls():
    """Test a maze with walls that require path navigation"""
    maze = [
        [0, 0, 0, 0],
        [2, 1, 0, 3],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    # One possible valid shortest path
    assert len(path) == 6

def test_no_path_maze():
    """Test a maze where no path exists"""
    maze = [
        [2, 1, 0],
        [1, 1, 0],
        [0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_start_or_end_missing():
    """Test maze without start or end cell"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_single_cell_path():
    """Test a maze with start and end in the same cell"""
    maze = [
        [2, 0, 0],
        [0, 0, 0],
        [0, 0, 3]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert len(path) > 1  # Path should include multiple cells
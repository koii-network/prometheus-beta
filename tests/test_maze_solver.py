import pytest
from src.maze_solver import solve_maze

def test_simple_maze():
    """Test a simple maze with a straightforward path"""
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = solve_maze(maze)
    assert path == [(0, 1), (1, 1), (1, 2)]

def test_maze_with_obstacles():
    """Test a maze with obstacles blocking direct path"""
    maze = [
        [2, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 3]
    ]
    path = solve_maze(maze)
    assert path == [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]

def test_no_path_exists():
    """Test maze where no path exists to the end"""
    maze = [
        [2, 1, 0],
        [1, 1, 1],
        [0, 0, 3]
    ]
    path = solve_maze(maze)
    assert path == []

def test_start_at_end():
    """Test maze where start and end are the same cell"""
    maze = [
        [0, 0, 0],
        [0, 3, 2],
        [0, 0, 0]
    ]
    path = solve_maze(maze)
    assert path == [(1, 2)]

def test_no_start_or_end():
    """Test maze without start or end cell"""
    maze = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    path = solve_maze(maze)
    assert path == []
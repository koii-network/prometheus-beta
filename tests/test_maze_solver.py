import pytest
from src.maze_solver import find_shortest_path

def test_basic_path():
    """Test a simple maze with a clear path"""
    maze = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == 5

def test_no_path():
    """Test a maze with no possible path"""
    maze = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
    assert find_shortest_path(maze) == -1

def test_start_blocked():
    """Test when start position is blocked"""
    maze = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == -1

def test_end_blocked():
    """Test when end position is blocked"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(maze) == -1

def test_single_cell_maze():
    """Test a single cell maze"""
    maze = [[0]]
    assert find_shortest_path(maze) == 1

def test_large_maze():
    """Test a larger maze with a path"""
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    assert find_shortest_path(maze) == 9

def test_empty_maze():
    """Test an empty maze"""
    maze = []
    assert find_shortest_path(maze) == -1

def test_invalid_maze_input():
    """Test raising ValueError for non-square maze"""
    with pytest.raises(ValueError):
        maze = [
            [0, 0, 0],
            [0, 0],
            [0, 0, 0]
        ]
        find_shortest_path(maze)
import pytest
from src.maze_solver import find_shortest_path

def test_basic_maze():
    """Test a simple maze with a clear path"""
    maze = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == 4

def test_no_path_blocked_start():
    """Test maze with blocked start"""
    maze = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) == -1

def test_no_path_blocked_end():
    """Test maze with blocked end"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(maze) == -1

def test_diagonal_movement():
    """Test diagonal movement is allowed"""
    maze = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert find_shortest_path(maze) == 3

def test_single_cell_maze():
    """Test a single cell maze"""
    maze = [[0]]
    assert find_shortest_path(maze) == 1

def test_empty_maze():
    """Test empty maze raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_irregular_maze():
    """Test maze with irregular row lengths"""
    maze = [
        [0, 0],
        [0, 0, 0],
        [0, 0]
    ]
    with pytest.raises(ValueError):
        find_shortest_path(maze)

def test_complex_maze():
    """Test a more complex maze with multiple paths"""
    maze = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(maze) == 7

def test_large_maze():
    """Test a larger maze with diagonal movements"""
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    assert find_shortest_path(maze) == 9
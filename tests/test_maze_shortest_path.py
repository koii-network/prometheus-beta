import pytest
from src.maze_shortest_path import shortest_path_in_maze

def test_basic_path():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert shortest_path_in_maze(grid) == 5  # Path length: top-left to bottom-right

def test_blocked_start():
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert shortest_path_in_maze(grid) == -1  # Start is blocked

def test_blocked_end():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert shortest_path_in_maze(grid) == -1  # End is blocked

def test_blocked_path():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Path exists, but will not be the shortest direct route
    assert shortest_path_in_maze(grid) == 5

def test_empty_grid():
    grid = []
    assert shortest_path_in_maze(grid) == -1

def test_single_cell_grid():
    grid = [[0]]
    assert shortest_path_in_maze(grid) == 1

def test_large_grid_no_path():
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    assert shortest_path_in_maze(grid) == -1

def test_obstacles_around_edges():
    grid = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    assert shortest_path_in_maze(grid) == 3
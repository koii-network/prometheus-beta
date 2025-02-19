import pytest
from src.maze_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_no_path_blocked_start():
    grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_no_path_blocked_end():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid) == -1

def test_single_cell_grid():
    grid = [[0]]
    assert find_shortest_path(grid) == 1

def test_single_cell_blocked_grid():
    grid = [[1]]
    assert find_shortest_path(grid) == -1

def test_empty_grid():
    grid = []
    assert find_shortest_path(grid) == -1

def test_complex_path():
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 7
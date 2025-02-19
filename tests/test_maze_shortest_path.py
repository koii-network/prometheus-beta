import pytest
from src.maze_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4  # shortest path is 4 steps

def test_blocked_start():
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1  # start is blocked

def test_blocked_end():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid) == -1  # end is blocked

def test_walls_in_path():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4  # path around walls

def test_no_path():
    grid = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1  # no valid path

def test_single_cell():
    grid = [[0]]
    assert find_shortest_path(grid) == 0  # single cell is start and end

def test_empty_grid():
    grid = []
    assert find_shortest_path(grid) == -1  # empty grid

def test_large_grid():
    grid = [[0]*10 for _ in range(10)]
    assert find_shortest_path(grid) == 18  # diagonal path length in 10x10 grid
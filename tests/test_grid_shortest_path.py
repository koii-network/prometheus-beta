import pytest
from src.grid_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

def test_with_obstacles():
    grid = [
        ['.', '.', '.'],
        ['.', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

def test_blocked_start():
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_blocked_end():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_no_path_possible():
    grid = [
        ['.', 'O', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_single_cell():
    grid = [
        ['.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]

def test_empty_grid():
    grid = []
    path = find_shortest_path(grid)
    assert path == []
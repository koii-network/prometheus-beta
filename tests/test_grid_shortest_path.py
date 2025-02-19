import pytest
from src.grid_shortest_path import find_shortest_path

def test_basic_shortest_path():
    grid = [
        ['.', '.', '.'],
        ['.', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

def test_no_path_blocked_start():
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_no_path_blocked_end():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_complex_path():
    grid = [
        ['.', '.', '.', '.'],
        ['.', 'O', 'O', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]

def test_empty_grid():
    grid = []
    path = find_shortest_path(grid)
    assert path == []

def test_single_cell_grid():
    grid = [['.']]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]
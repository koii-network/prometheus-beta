import pytest
from src.grid_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert len(path) == 5  # 4 moves + start point
    assert path[0] == (0, 0) and path[-1] == (2, 2)

def test_blocked_grid():
    grid = [
        ['.', 'O', '.'],
        ['O', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == []  # No path should exist

def test_start_blocked():
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_end_blocked():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path == []

def test_complex_blocked_grid():
    grid = [
        ['.', '.', '.', '.'],
        ['O', 'O', '.', '.'],
        ['.', '.', 'O', '.'],
        ['.', '.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert len(path) == 7  # 6 moves + start point
    assert path[0] == (0, 0) and path[-1] == (3, 3)

def test_empty_grid():
    grid = []
    path = find_shortest_path(grid)
    assert path == []
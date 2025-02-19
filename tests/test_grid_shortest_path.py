import pytest
from src.grid_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        ['.', '.', '.'],
        ['.', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 5  # Minimal path length
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_blocked_start():
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_blocked_end():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_completely_blocked():
    grid = [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_empty_grid():
    grid = []
    path = find_shortest_path(grid)
    assert path is None

def test_complex_path():
    grid = [
        ['.', '.', '.', '.'],
        ['O', 'O', '.', '.'],
        ['.', '.', '.', 'O'],
        ['.', 'O', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) <= 7  # Ensure a reasonably short path
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)

def test_single_cell_grid():
    grid = [['.']]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]
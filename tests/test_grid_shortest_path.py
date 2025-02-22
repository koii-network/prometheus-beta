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
    assert len(path) == 5  # From (0,0) to (2,2)
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_blocked_start_end():
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_no_path_exists():
    grid = [
        ['.', 'O', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_empty_grid():
    grid = []
    path = find_shortest_path(grid)
    assert path is None

def test_single_cell_grid():
    grid = [['.']]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]

def test_rectangular_grid():
    grid = [
        ['.', '.', '.', '.'],
        ['.', 'O', 'O', '.'],
        ['.', '.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 7  # Path from (0,0) to (2,3)
    assert path[0] == (0, 0)
    assert path[-1] == (2, 3)

def test_complex_path():
    grid = [
        ['.', 'O', '.', '.'],
        ['.', '.', 'O', '.'],
        ['O', '.', '.', '.'],
        ['.', '.', 'O', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) > 0
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)
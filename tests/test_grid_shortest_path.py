import pytest
from src.grid_shortest_path import find_shortest_path

def test_basic_path():
    # Simple grid with clear path
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 5

def test_blocked_path():
    # Grid with blocked paths
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 5

def test_impossible_path():
    # Grid with no possible path
    grid = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_single_cell_grid():
    # Single cell grid
    grid = [[0]]
    assert find_shortest_path(grid) == 1

def test_empty_grid():
    # Empty grid
    grid = []
    assert find_shortest_path(grid) == -1

def test_large_grid():
    # Larger grid with a path
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert find_shortest_path(grid) == 7

def test_complex_path():
    # Complex grid with specific path requirements
    grid = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 7
import pytest
from src.grid_path_finder import find_shortest_grid_path

def test_simple_path():
    """Test a simple grid with a clear path"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_grid_path(grid) == 5

def test_blocked_start():
    """Test when start cell is blocked"""
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_grid_path(grid) is None

def test_blocked_end():
    """Test when end cell is blocked"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_grid_path(grid) is None

def test_partial_blocked_path():
    """Test a grid with some blocked cells requiring detour"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_grid_path(grid) == 5

def test_complex_blocked_path():
    """Test a more complex grid with multiple blocked cells"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    assert find_shortest_grid_path(grid) == 7

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [[0]]
    assert find_shortest_grid_path(grid) == 1

def test_empty_grid():
    """Test empty grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_grid_path([])

def test_non_square_grid():
    """Test non-square grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_grid_path([
            [0, 0, 0],
            [0, 0]
        ])

def test_large_grid():
    """Test a larger grid with more complex pathing"""
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    assert find_shortest_grid_path(grid) == 9
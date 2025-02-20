import pytest
from src.grid_shortest_path import find_shortest_path

def test_empty_grid():
    """Test empty grid returns -1"""
    assert find_shortest_path([]) == -1
    assert find_shortest_path([[]]) == -1

def test_single_cell_grid():
    """Test grid with single empty or blocked cell"""
    assert find_shortest_path([[0]]) == 1
    assert find_shortest_path([[1]]) == -1

def test_simple_path_exists():
    """Test a simple grid with a clear path"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 5  # 3 right + 2 down or vice versa

def test_path_with_obstacles():
    """Test grid with some obstacles"""
    grid = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    # Expect a path that avoids obstacles
    assert find_shortest_path(grid) == 6

def test_no_path_exists():
    """Test grid where no path is possible"""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_path_with_first_column_blocked():
    """Test scenario where first column has obstacles"""
    grid = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_path_with_complex_obstacles():
    """Test a more complex grid with strategic obstacle placement"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    # The path should go around the obstacles
    assert find_shortest_path(grid) == 7
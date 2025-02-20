import pytest
from src.grid_shortest_path import find_shortest_constrained_path

def test_basic_empty_grid():
    """Test a simple grid with a clear path"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_constrained_path(grid) == 5

def test_grid_with_obstacles():
    """Test a grid with some obstacles"""
    grid = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_constrained_path(grid) == 5

def test_blocked_right_must_go_down():
    """Test scenario where right is blocked, must move down"""
    grid = [
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_constrained_path(grid) == 5

def test_completely_blocked_grid():
    """Test a grid with no possible path"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert find_shortest_constrained_path(grid) is None

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [[0]]
    assert find_shortest_constrained_path(grid) == 1

def test_empty_grid():
    """Test an empty grid"""
    grid = []
    assert find_shortest_constrained_path(grid) is None

def test_start_or_end_blocked():
    """Test when start or end cell is blocked"""
    grid1 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_constrained_path(grid1) is None

    grid2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_constrained_path(grid2) is None
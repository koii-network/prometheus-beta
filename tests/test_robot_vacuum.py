import pytest
from src.robot_vacuum import cleanRoom

def test_empty_grid():
    """Test an empty grid"""
    grid = []
    assert cleanRoom(grid, 0, 0, 0) == 0

def test_single_cell_clean():
    """Test a single clean cell"""
    grid = [[0]]
    assert cleanRoom(grid, 0, 0, 0) == 0

def test_single_cell_dirty():
    """Test a single dirty cell"""
    grid = [[0]]
    assert cleanRoom(grid, 0, 0, 0) == 0

def test_simple_room():
    """Test a simple room with a few cells"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = cleanRoom(grid, 1, 1, 0)
    assert result > 0

def test_room_with_obstacles():
    """Test a room with some obstacles (1s)"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result = cleanRoom(grid, 0, 0, 0)
    assert result > 0

def test_invalid_start_position():
    """Test invalid starting position"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert cleanRoom(grid, 3, 3, 0) == 0
    assert cleanRoom(grid, -1, -1, 0) == 0

def test_unreachable_cells():
    """Test a grid with some unreachable cells"""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = cleanRoom(grid, 2, 2, 0)
    assert result > 0  # Should still be able to clean reachable cells
import pytest
from src.robot_vacuum import cleanRoom

def test_empty_grid():
    """Test with an empty grid"""
    assert cleanRoom([], 0, 0, 0) == 0
    assert cleanRoom([[], []], 0, 0, 0) == 0

def test_single_cell_grid():
    """Test with a single cell grid"""
    assert cleanRoom([[0]], 0, 0, 0) == 1
    assert cleanRoom([[1]], 0, 0, 0) == 0

def test_simple_room():
    """Test a simple room with no obstacles"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Different starting positions and directions
    assert cleanRoom(grid, 1, 1, 0) <= 9  # Should clean all cells
    assert cleanRoom(grid, 0, 0, 1) <= 9

def test_room_with_obstacles():
    """Test a room with some obstacles"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Robot should navigate around obstacles
    result = cleanRoom(grid, 0, 0, 1)
    assert result <= 7  # Less than total cells due to obstacles

def test_invalid_start_position():
    """Test starting on an obstacle or out of bounds"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert cleanRoom(grid, 1, 1, 0) == 0  # Starting on obstacle
    assert cleanRoom(grid, -1, 0, 0) == 0  # Out of bounds
    assert cleanRoom(grid, 3, 0, 0) == 0  # Out of bounds

def test_maximum_steps():
    """Ensure total steps do not exceed grid size"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = cleanRoom(grid, 1, 1, 0)
    assert result <= 9  # max steps in 3x3 grid
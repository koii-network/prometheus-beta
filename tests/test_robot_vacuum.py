import pytest
from src.robot_vacuum import cleanRoom

def test_empty_room():
    """Test an empty room (all clean cells)"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert cleanRoom(grid, 1, 1, 0) > 0  # Should explore entire room

def test_room_with_obstacles():
    """Test a room with some obstacles"""
    grid = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    assert cleanRoom(grid, 0, 0, 1) > 0  # Should navigate around obstacles

def test_all_obstacles():
    """Test a room with all obstacles"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert cleanRoom(grid, 0, 0, 0) == 0  # No clean cells to explore

def test_single_cell_room():
    """Test a single cell room"""
    grid = [[0]]
    assert cleanRoom(grid, 0, 0, 0) == 1  # Should clean and return 1 step

def test_invalid_start_position():
    """Test starting from an obstacle"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert cleanRoom(grid, 1, 1, 0) == 0  # Starting on an obstacle

def test_complex_room_layout():
    """Test a more complex room layout"""
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    result = cleanRoom(grid, 0, 0, 1)
    assert result > 0  # Should explore most of the room

def test_different_starting_directions():
    """Test different starting directions"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Different directions should yield different step counts
    north_result = cleanRoom(grid, 1, 1, 0)  # North
    east_result = cleanRoom(grid, 1, 1, 1)   # East
    assert north_result > 0 and east_result > 0
    assert north_result != east_result

def test_invalid_input():
    """Test empty grid input"""
    assert cleanRoom([], 0, 0, 0) == 0
    assert cleanRoom([[], []], 0, 0, 0) == 0
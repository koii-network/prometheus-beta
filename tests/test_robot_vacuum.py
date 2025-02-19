import pytest
from src.robot_vacuum import cleanRoom

def test_empty_room():
    """Test cleaning an empty room"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps == 9  # All 9 cells must be cleaned

def test_room_with_obstacles():
    """Test cleaning a room with obstacles"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps < 9  # Some cells blocked, fewer steps

def test_single_cell_room():
    """Test cleaning a single-cell room"""
    grid = [[0]]
    steps = cleanRoom(grid, 0, 0, 0)
    assert steps == 1  # Only one cell to clean

def test_no_move_possible():
    """Test a room with no valid moves"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    steps = cleanRoom(grid, 0, 0, 0)
    assert steps == 0  # No valid moves

def test_different_starting_positions():
    """Test cleaning from different starting positions"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Different starting positions and directions
    test_cases = [
        (0, 0, 0),   # Top-left, facing North
        (2, 2, 2),   # Bottom-right, facing South
        (1, 1, 1),   # Center, facing East
        (0, 2, 3)    # Top-right, facing West
    ]
    
    for r, c, direction in test_cases:
        steps = cleanRoom(grid, r, c, direction)
        assert steps == 9  # All cells cleaned regardless of start
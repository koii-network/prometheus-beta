import pytest
from src.robot_vacuum import cleanRoom

def test_clean_empty_room():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Starting from center, facing right
    steps = cleanRoom(grid, 1, 1, 1)
    assert steps > 0 and steps <= 9  # Should clean entire room

def test_room_with_blocked_cells():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Starting from top-left, facing down
    steps = cleanRoom(grid, 0, 0, 2)
    assert steps > 0 and steps <= 6  # Can navigate around blocked cells

def test_impossible_to_clean_room():
    grid = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    # Isolated cell in the center
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps == -1  # Cannot clean rooms with inaccessible cells

def test_single_cell_room():
    grid = [[0]]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == 0  # Already cleaned single cell

def test_rectangular_room():
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # Different room shape and starting position
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps > 0 and steps <= 8
import pytest
from src.robot_vacuum import cleanRoom

def test_empty_grid():
    grid = []
    assert cleanRoom(grid, 0, 0, 'N') == 0

def test_single_cell_grid():
    grid = [[0]]
    assert cleanRoom(grid, 0, 0, 'N') == 0

def test_simple_room_cleaning():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 'N')
    assert steps == 8  # Number of adjacent empty cells

def test_grid_with_obstacles():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 'E')
    assert steps == 6  # Number of non-obstacle cells

def test_invalid_starting_position_out_of_bounds():
    grid = [[0, 0], [0, 0]]
    with pytest.raises(ValueError, match="Invalid starting position"):
        cleanRoom(grid, 2, 0, 'N')

def test_invalid_starting_position_obstacle():
    grid = [[0, 1], [0, 0]]
    with pytest.raises(ValueError, match="Invalid starting position"):
        cleanRoom(grid, 0, 1, 'N')

def test_grid_with_larger_obstacles():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 'E')
    assert steps == 9  # Number of non-obstacle cells
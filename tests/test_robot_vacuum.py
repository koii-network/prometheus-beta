import pytest
from src.robot_vacuum import cleanRoom

def test_basic_room_cleaning():
    """Test cleaning a simple room with no obstacles."""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps > 0  # Should take some steps to clean

def test_room_with_obstacles():
    """Test room with some obstacles."""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps > 0  # Should navigate around obstacle

def test_inaccessible_room():
    """Test a room where not all cells are reachable."""
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == -1  # Cannot clean entire room

def test_starting_on_obstacle():
    """Test starting on an obstacle."""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps == 0  # Starting on obstacle

def test_input_validation():
    """Test invalid input handling."""
    # Empty grid
    with pytest.raises(ValueError):
        cleanRoom([], 0, 0, 0)
    
    # Out of bounds starting position
    with pytest.raises(ValueError):
        grid = [[0, 0], [0, 0]]
        cleanRoom(grid, 2, 2, 0)
    
    # Invalid direction
    with pytest.raises(ValueError):
        grid = [[0, 0], [0, 0]]
        cleanRoom(grid, 0, 0, 4)

def test_different_directions():
    """Test cleaning with different starting directions."""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Try different starting directions
    for direction in range(4):
        steps = cleanRoom(grid, 1, 1, direction)
        assert steps > 0
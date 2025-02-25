import pytest
from src.robot_vacuum import cleanRoom

def test_simple_room():
    """Test a simple empty room"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps == 8  # Should visit all cells

def test_room_with_obstacles():
    """Test a room with obstacles"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == 7  # Avoid the obstacle

def test_edge_cases():
    """Test various edge cases"""
    # Test starting at corner
    grid = [
        [0, 0],
        [0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == 3

def test_invalid_inputs():
    """Test invalid input handling"""
    # Empty grid
    with pytest.raises(ValueError):
        cleanRoom([], 0, 0, 0)
    
    # Out of bounds position
    with pytest.raises(ValueError):
        grid = [[0, 0], [0, 0]]
        cleanRoom(grid, 2, 2, 0)
    
    # Invalid direction
    with pytest.raises(ValueError):
        grid = [[0, 0], [0, 0]]
        cleanRoom(grid, 0, 0, 4)

def test_grid_with_more_obstacles():
    """Test a more complex grid with multiple obstacles"""
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps >= 6  # Exact number might vary, but should visit most cells
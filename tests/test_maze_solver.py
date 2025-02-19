import pytest
from src.maze_solver import find_shortest_path, get_neighbors, is_valid

def test_find_shortest_path_basic():
    """Test a simple maze with a direct path"""
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(1, 0), (1, 1), (1, 2)]

def test_find_shortest_path_complex():
    """Test a more complex maze with obstacles"""
    maze = [
        [0, 0, 0, 0],
        [2, 1, 0, 0],
        [0, 1, 0, 3],
        [0, 1, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    # Validate path reaches end from start
    assert path[0] == (1, 0)  # Start
    assert path[-1] == (2, 3)  # End

def test_no_path_exists():
    """Test scenario where no path exists"""
    maze = [
        [2, 1, 0],
        [1, 1, 0],
        [0, 1, 3]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_start_or_end_missing():
    """Test when start or end cell is missing"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_get_neighbors():
    """Test the get_neighbors function"""
    cell = (1, 1)
    neighbors = get_neighbors(cell)
    assert set(neighbors) == {(0, 1), (1, 2), (2, 1), (1, 0)}

def test_is_valid():
    """Test the is_valid function"""
    maze = [
        [0, 1, 0],
        [0, 0, 0],
        [1, 1, 1]
    ]
    assert is_valid((0, 0), maze) is True  # Valid empty cell
    assert is_valid((0, 1), maze) is False  # Wall cell
    assert is_valid((2, 0), maze) is False  # Wall cell
    assert is_valid((-1, 0), maze) is False  # Out of bounds
    assert is_valid((3, 0), maze) is False  # Out of bounds
import pytest
from src.maze_shortest_path import find_shortest_path, get_neighbors, is_valid

def test_get_neighbors():
    """Test the get_neighbors function"""
    cell = (2, 3)
    expected_neighbors = [(1, 3), (2, 4), (3, 3), (2, 2)]
    assert get_neighbors(cell) == expected_neighbors

def test_is_valid():
    """Test the is_valid function"""
    maze = [
        [0, 1, 0],
        [2, 0, 3],
        [1, 0, 1]
    ]
    
    # Valid cells
    assert is_valid((0, 0), maze) == True  # Empty cell
    assert is_valid((1, 2), maze) == True  # End cell
    
    # Invalid cells
    assert is_valid((0, 1), maze) == False  # Wall
    assert is_valid((-1, 0), maze) == False  # Out of bounds
    assert is_valid((3, 0), maze) == False  # Out of bounds

def test_find_shortest_path_simple():
    """Test finding shortest path in a simple maze"""
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    expected_path = [(1, 0), (1, 1), (1, 2)]
    assert find_shortest_path(maze) == expected_path

def test_find_shortest_path_complex():
    """Test finding shortest path in a more complex maze"""
    maze = [
        [0, 0, 0, 0],
        [2, 1, 1, 3],
        [0, 0, 0, 0]
    ]
    expected_path = [(1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]
    assert find_shortest_path(maze) == expected_path

def test_find_shortest_path_no_path():
    """Test scenario where no path exists"""
    maze = [
        [1, 1, 1],
        [2, 1, 3],
        [1, 1, 1]
    ]
    assert find_shortest_path(maze) is None

def test_find_shortest_path_no_start_or_end():
    """Test scenario where start or end is missing"""
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(maze) is None
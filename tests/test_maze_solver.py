import pytest
from src.maze_solver import find_shortest_path

def test_simple_path():
    # Simple maze with direct path
    maze = [
        [0, 0, 0],
        [2, 0, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert path == [(1, 0), (1, 1), (1, 2)]

def test_path_with_obstacles():
    # Maze with walls requiring navigation
    maze = [
        [0, 0, 0, 0],
        [2, 1, 1, 3],
        [0, 0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert len(path) == 5
    assert path[0] == (1, 0)
    assert path[-1] == (1, 3)

def test_no_path_exists():
    # Maze with no possible path
    maze = [
        [1, 1, 1],
        [2, 1, 3],
        [1, 1, 1]
    ]
    path = find_shortest_path(maze)
    assert path is None

def test_multiple_possible_paths():
    # Maze with multiple possible paths
    maze = [
        [0, 0, 0],
        [2, 1, 3],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is not None
    assert len(path) == 3

def test_no_start_or_end():
    # Maze without start or end
    maze = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path is None
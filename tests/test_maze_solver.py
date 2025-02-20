import pytest
from src.maze_solver import find_shortest_path

def test_simple_path_exists():
    maze = [
        ['.', '.', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(maze, (0, 0), (2, 2))
    assert path is not None
    assert len(path) == 5  # Shortest path length
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_no_path_exists():
    maze = [
        ['.', '#', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(maze, (0, 0), (2, 2))
    assert path is None

def test_start_or_end_on_wall():
    maze = [
        ['.', '.', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    # Start on wall
    path1 = find_shortest_path(maze, (1, 0), (2, 2))
    assert path1 is None
    
    # End on wall
    path2 = find_shortest_path(maze, (0, 0), (1, 1))
    assert path2 is None

def test_empty_maze():
    maze = []
    path = find_shortest_path(maze, (0, 0), (0, 0))
    assert path is None

def test_out_of_bounds():
    maze = [
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(maze, (-1, 0), (3, 3))
    assert path is None

def test_same_start_and_end():
    maze = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(maze, (1, 1), (1, 1))
    assert path == [(1, 1)]
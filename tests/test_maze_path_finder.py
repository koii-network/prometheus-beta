import pytest
from src.maze_path_finder import find_shortest_path

def test_basic_path_finder():
    maze = [
        ['.', '.', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) == 5  # Number of steps in the shortest path
    assert path[0] == start
    assert path[-1] == end

def test_no_path_exists():
    maze = [
        ['.', '#', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_start_at_wall():
    maze = [
        ['#', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_end_at_wall():
    maze = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '#']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_out_of_bounds():
    maze = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    start = (-1, 0)
    end = (3, 3)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_empty_maze():
    maze = []
    start = (0, 0)
    end = (0, 0)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_multiple_possible_paths():
    maze = [
        ['.', '.', '.', '.'],
        ['#', '#', '.', '#'],
        ['.', '.', '.', '.'']
    ]
    start = (0, 0)
    end = (2, 3)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) >= 6 and len(path) <= 7  # Allow for slight variations in shortest path
    assert path[0] == start
    assert path[-1] == end
import pytest
from src.maze_shortest_path import find_shortest_path

def test_basic_path():
    maze = [
        ['.', '.', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) == 5  # Minimum path length
    assert path[0] == start
    assert path[-1] == end

def test_no_path():
    maze = [
        ['.', '#', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_start_wall():
    maze = [
        ['#', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_end_wall():
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
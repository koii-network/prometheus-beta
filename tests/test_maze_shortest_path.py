import pytest
from src.maze_shortest_path import find_shortest_path

def test_basic_maze_path():
    maze = [
        ['.', '.', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) == 5  # Direct path
    assert path[0] == start
    assert path[-1] == end

def test_maze_with_single_path():
    maze = [
        ['.', '.', '.', '.'],
        ['#', '#', '#', '.'],
        ['.', '.', '.', '.']
    ]
    start = (0, 0)
    end = (2, 3)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) == 7
    assert path[0] == start
    assert path[-1] == end

def test_no_path_exists():
    maze = [
        ['.', '#', '.'],
        ['#', '#', '.'],
        ['.', '#', '.']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
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
    start = (0, 0)
    end = (0, 0)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_out_of_bounds():
    maze = [
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    # Start out of bounds
    path1 = find_shortest_path(maze, (2, 0), (1, 1))
    assert path1 is None
    
    # End out of bounds
    path2 = find_shortest_path(maze, (0, 0), (2, 3))
    assert path2 is None
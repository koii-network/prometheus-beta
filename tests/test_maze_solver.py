import pytest
from src.maze_solver import find_shortest_path

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
    assert len(path) == 5  # Path length including start and end
    assert path[0] == start
    assert path[-1] == end

def test_no_path_maze():
    maze = [
        ['.', '#', '.'],
        ['#', '#', '.'],
        ['.', '.', '.']
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

def test_invalid_maze_input():
    # Empty maze
    path1 = find_shortest_path([], (0, 0), (0, 0))
    assert path1 is None
    
    # Out of bounds start/end
    maze = [['.', '.']]
    path2 = find_shortest_path(maze, (-1, 0), (0, 2))
    assert path2 is None

def test_single_cell_maze():
    maze = [['.']]
    start = (0, 0)
    end = (0, 0)
    
    path = find_shortest_path(maze, start, end)
    assert path == [(0, 0)]
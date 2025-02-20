import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from maze_shortest_path import find_shortest_path

def test_simple_open_maze():
    maze = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path == [(0,0), (1,1), (2,2)]

def test_maze_with_wall_blocking_direct_path():
    maze = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert len(path) > 0  # Ensure path exists
    assert path[0] == (0,0) and path[-1] == (2,2)

def test_no_path_possible():
    maze = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert path == []

def test_start_or_end_blocked():
    start_blocked = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    end_blocked = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(start_blocked) == []
    assert find_shortest_path(end_blocked) == []

def test_large_maze():
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    path = find_shortest_path(maze)
    assert len(path) > 0  # Ensure path exists
    assert path[0] == (0,0) and path[-1] == (4,4)

def test_empty_maze():
    assert find_shortest_path([]) == []
    assert find_shortest_path([[]]) == []
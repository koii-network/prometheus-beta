import pytest
from src.grid_path_finder import find_shortest_path

def test_simple_path():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0,0), (0,1), (0,2), (1,2), (2,2)]

def test_single_cell_grid():
    grid = [['.']]
    path = find_shortest_path(grid)
    assert path == [(0,0)]

def test_path_with_obstacles():
    grid = [
        ['.', '.', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0,0), (0,1), (0,2), (1,2), (2,2)]

def test_no_path_exists():
    grid = [
        ['.', 'O', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    with pytest.raises(ValueError, match="No path exists"):
        find_shortest_path(grid)

def test_empty_grid():
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        find_shortest_path([])

def test_non_square_grid():
    grid = [
        ['.', '.'],
        ['.']
    ]
    with pytest.raises(ValueError, match="Grid must be square"):
        find_shortest_path(grid)

def test_complex_grid():
    grid = [
        ['.', '.', '.', '.'],
        ['O', 'O', '.', '.'],
        ['.', '.', 'O', '.'],
        ['.', 'O', '.', '.']
    ]
    path = find_shortest_path(grid)
    # Verify path exists and reaches end
    assert path[0] == (0,0)
    assert path[-1] == (3,3)
    assert len(path) > 0
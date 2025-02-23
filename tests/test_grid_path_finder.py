import pytest
from src.grid_path_finder import find_shortest_path

def test_simple_path():
    """Test a simple grid with a clear path"""
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 5  # Shortest path in 3x3 grid
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_blocked_path():
    """Test a grid with some blocked cells"""
    grid = [
        ['.', '.', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 5  # Should still find a path around obstacles
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_no_path():
    """Test a grid with no possible path"""
    grid = [
        ['.', 'O', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [['.']]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]

def test_empty_grid():
    """Test empty grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_non_square_grid():
    """Test non-square grid raises ValueError"""
    grid = [
        ['.', '.'],
        ['.', '.', '.']
    ]
    with pytest.raises(ValueError):
        find_shortest_path(grid)

def test_complex_path():
    """Test a more complex grid with multiple possible paths"""
    grid = [
        ['.', '.', '.', '.'],
        ['O', 'O', '.', '.'],
        ['.', '.', '.', 'O'],
        ['.', 'O', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 7  # Path length depends on avoiding obstacles
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)
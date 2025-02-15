import pytest
from src.unique_grid_paths import count_unique_paths

def test_basic_grid_paths():
    # Test some standard grid sizes
    assert count_unique_paths(2, 2) == 2  # 2x2 grid
    assert count_unique_paths(3, 3) == 6  # 3x3 grid
    assert count_unique_paths(3, 7) == 28  # 3x7 grid

def test_single_row_or_column():
    # Test grids with single row or column (only one path possible)
    assert count_unique_paths(1, 5) == 1
    assert count_unique_paths(5, 1) == 1

def test_invalid_input():
    # Test invalid grid dimensions
    with pytest.raises(ValueError):
        count_unique_paths(0, 5)
    with pytest.raises(ValueError):
        count_unique_paths(5, 0)
    with pytest.raises(ValueError):
        count_unique_paths(-1, 5)

def test_minimum_grid():
    # Test 1x1 grid
    assert count_unique_paths(1, 1) == 1
import pytest
from src.unique_grid_paths import count_unique_paths

def test_count_unique_paths_standard_grid():
    """Test a standard grid size"""
    assert count_unique_paths(3, 7) == 28

def test_count_unique_paths_single_row():
    """Test a grid with a single row"""
    assert count_unique_paths(1, 5) == 1

def test_count_unique_paths_single_column():
    """Test a grid with a single column"""
    assert count_unique_paths(5, 1) == 1

def test_count_unique_paths_two_by_two():
    """Test a 2x2 grid"""
    assert count_unique_paths(2, 2) == 2

def test_count_unique_paths_invalid_input():
    """Test that invalid grid dimensions raise a ValueError"""
    with pytest.raises(ValueError):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError):
        count_unique_paths(-1, 5)

def test_count_unique_paths_one_by_one():
    """Test a 1x1 grid"""
    assert count_unique_paths(1, 1) == 1
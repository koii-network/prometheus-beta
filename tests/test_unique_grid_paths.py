import pytest
from src.unique_grid_paths import count_unique_paths

def test_unique_paths_3x2_grid():
    """Test unique paths for a 3x2 grid"""
    assert count_unique_paths(3, 2) == 3

def test_unique_paths_7x3_grid():
    """Test unique paths for a 7x3 grid"""
    assert count_unique_paths(7, 3) == 28

def test_unique_paths_1x1_grid():
    """Test unique paths for a 1x1 grid"""
    assert count_unique_paths(1, 1) == 1

def test_unique_paths_invalid_inputs():
    """Test that invalid grid dimensions raise ValueError"""
    with pytest.raises(ValueError):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError):
        count_unique_paths(-1, 5)
    
    with pytest.raises(ValueError):
        count_unique_paths(5, -1)
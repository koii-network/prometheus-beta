import pytest
from src.unique_grid_paths import count_unique_paths

def test_standard_grid_paths():
    """Test paths for common grid sizes"""
    assert count_unique_paths(2, 3) == 3
    assert count_unique_paths(3, 2) == 3
    assert count_unique_paths(3, 3) == 6

def test_single_row_column():
    """Test paths for single row or column grids"""
    assert count_unique_paths(1, 5) == 1
    assert count_unique_paths(5, 1) == 1

def test_large_grid():
    """Test paths for larger grid"""
    assert count_unique_paths(10, 10) == 48620

def test_small_grid():
    """Test paths for small grid"""
    assert count_unique_paths(1, 1) == 1

def test_invalid_input():
    """Test error handling for invalid grid dimensions"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(-1, 5)
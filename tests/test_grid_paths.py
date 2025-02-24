import pytest
from src.grid_paths import count_unique_paths

def test_basic_grid_paths():
    """Test basic scenarios with small grid sizes"""
    assert count_unique_paths(2, 2) == 2, "2x2 grid should have 2 unique paths"
    assert count_unique_paths(3, 3) == 6, "3x3 grid should have 6 unique paths"
    assert count_unique_paths(3, 2) == 3, "3x2 grid should have 3 unique paths"

def test_single_row_or_column():
    """Test grids with single row or single column"""
    assert count_unique_paths(1, 5) == 1, "1xN grid should have 1 unique path"
    assert count_unique_paths(5, 1) == 1, "Nx1 grid should have 1 unique path"

def test_large_grid():
    """Test larger grid sizes"""
    assert count_unique_paths(10, 10) == 48620, "10x10 grid path count incorrect"
    assert count_unique_paths(15, 15) == 155117520, "15x15 grid path count incorrect"

def test_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(-1, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, -3)
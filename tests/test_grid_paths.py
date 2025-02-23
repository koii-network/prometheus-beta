import pytest
from src.grid_paths import count_unique_paths

def test_basic_grid_paths():
    """Test basic grid path scenarios"""
    # 1x1 grid
    assert count_unique_paths(1, 1) == 1
    
    # 2x2 grid
    assert count_unique_paths(2, 2) == 2
    
    # 3x3 grid
    assert count_unique_paths(3, 3) == 6

def test_rectangular_grids():
    """Test paths in rectangular grids"""
    # Wider than tall
    assert count_unique_paths(2, 3) == 3
    
    # Taller than wide
    assert count_unique_paths(3, 2) == 3

def test_large_grid():
    """Test a larger grid"""
    assert count_unique_paths(10, 10) == 48620

def test_invalid_grid_inputs():
    """Test error handling for invalid grid dimensions"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(-1, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, -1)
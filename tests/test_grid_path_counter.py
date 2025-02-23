import pytest
from src.grid_path_counter import count_unique_paths

def test_standard_grid_sizes():
    """Test common grid sizes"""
    assert count_unique_paths(3, 7) == 28
    assert count_unique_paths(3, 2) == 3
    assert count_unique_paths(7, 3) == 28  # Symmetry check
    assert count_unique_paths(2, 3) == 3   # Symmetry check

def test_single_row_or_column():
    """Test grids with single row or column"""
    assert count_unique_paths(1, 5) == 1
    assert count_unique_paths(5, 1) == 1
    assert count_unique_paths(1, 1) == 1

def test_invalid_grid_sizes():
    """Test error handling for invalid grid sizes"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(-1, 5)
    
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, -1)

def test_large_grid():
    """Test a larger grid size"""
    # Verify a known large grid result
    assert count_unique_paths(10, 10) == 48620
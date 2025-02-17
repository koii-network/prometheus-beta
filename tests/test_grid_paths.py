import pytest
from src.grid_paths import count_unique_paths

def test_basic_grid_paths():
    """Test unique paths for a 2x3 grid"""
    assert count_unique_paths(2, 3) == 3

def test_square_grid():
    """Test unique paths for a square grid"""
    assert count_unique_paths(3, 3) == 6

def test_single_row_grid():
    """Test unique paths for a single row grid"""
    assert count_unique_paths(1, 5) == 1

def test_single_column_grid():
    """Test unique paths for a single column grid"""
    assert count_unique_paths(5, 1) == 1

def test_small_grid():
    """Test unique paths for a small 3x2 grid"""
    assert count_unique_paths(3, 2) == 3

def test_invalid_grid_zero_input():
    """Test that zero input raises ValueError"""
    with pytest.raises(ValueError):
        count_unique_paths(0, 5)

def test_invalid_grid_negative_input():
    """Test that negative input raises ValueError"""
    with pytest.raises(ValueError):
        count_unique_paths(-2, 3)
        
def test_invalid_grid_both_zero():
    """Test that both zero inputs raise ValueError"""
    with pytest.raises(ValueError):
        count_unique_paths(0, 0)
import pytest
from src.unique_grid_paths import count_unique_paths

def test_small_grid():
    """Test a small 2x2 grid"""
    assert count_unique_paths(2, 2) == 2

def test_rectangular_grid():
    """Test a rectangular grid"""
    assert count_unique_paths(3, 4) == 10

def test_single_row_grid():
    """Test a grid with single row"""
    assert count_unique_paths(1, 5) == 1

def test_single_column_grid():
    """Test a grid with single column"""
    assert count_unique_paths(5, 1) == 1

def test_large_grid():
    """Test a larger grid"""
    assert count_unique_paths(10, 10) == 48620

def test_invalid_grid_negative_rows():
    """Test invalid input with negative rows"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(-1, 5)

def test_invalid_grid_negative_columns():
    """Test invalid input with negative columns"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, -1)

def test_invalid_grid_zero_dimensions():
    """Test invalid input with zero dimensions"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(0, 0)
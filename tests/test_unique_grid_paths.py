import pytest
from src.unique_grid_paths import count_unique_paths

def test_standard_grid_sizes():
    assert count_unique_paths(2, 3) == 3  # 3 unique paths
    assert count_unique_paths(3, 2) == 3  # symmetric case
    assert count_unique_paths(3, 3) == 6  # slightly larger grid

def test_single_row_or_column():
    assert count_unique_paths(1, 5) == 1  # single row
    assert count_unique_paths(5, 1) == 1  # single column

def test_small_grid():
    assert count_unique_paths(1, 1) == 1  # smallest possible grid

def test_invalid_input():
    with pytest.raises(ValueError):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError):
        count_unique_paths(-1, 5)

def test_larger_grid():
    # Verify a larger grid calculation
    assert count_unique_paths(5, 5) == 70
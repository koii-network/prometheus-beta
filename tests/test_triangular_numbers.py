import pytest
from src.triangular_numbers import count_triangular_numbers

def test_count_triangular_numbers_basic():
    """Test basic cases of counting triangular numbers"""
    assert count_triangular_numbers(0) == 0
    assert count_triangular_numbers(1) == 1
    assert count_triangular_numbers(3) == 2  # 1, 3
    assert count_triangular_numbers(6) == 3  # 1, 3, 6
    assert count_triangular_numbers(10) == 4  # 1, 3, 6, 10

def test_count_triangular_numbers_large():
    """Test larger numbers"""
    assert count_triangular_numbers(100) == 13
    assert count_triangular_numbers(1000) == 44

def test_count_triangular_numbers_edge_cases():
    """Test edge cases"""
    assert count_triangular_numbers(0) == 0
    assert count_triangular_numbers(7) == 3  # 1, 3, 6

def test_count_triangular_numbers_invalid_input():
    """Test handling of negative inputs"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_triangular_numbers(-1)
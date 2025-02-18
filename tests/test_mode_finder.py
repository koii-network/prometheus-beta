import pytest
from src.mode_finder import find_mode

def test_single_mode():
    """Test finding a single mode"""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes"""
    result = find_mode([1, 2, 2, 3, 3, 4])
    assert set(result) == {2, 3}

def test_all_unique_numbers():
    """Test when all numbers appear once"""
    assert find_mode([1, 2, 3, 4, 5]) == 1

def test_empty_list():
    """Test empty list returns empty list"""
    assert find_mode([]) == []

def test_float_numbers():
    """Test mode works with float numbers"""
    result = find_mode([1.5, 2.3, 1.5, 3.7, 2.3])
    assert set(result) == {1.5, 2.3}

def test_invalid_input():
    """Test that invalid input raises TypeError"""
    with pytest.raises(TypeError):
        find_mode("not a list")
    with pytest.raises(TypeError):
        find_mode(123)
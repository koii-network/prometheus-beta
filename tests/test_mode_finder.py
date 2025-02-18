import pytest
from src.mode_finder import find_mode

def test_find_mode_single_mode():
    """Test finding a single mode"""
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([1.5, 2.3, 2.3, 3.1, 4.2]) == 2.3

def test_find_mode_multiple_modes():
    """Test finding multiple modes"""
    assert set(find_mode([1, 2, 2, 3, 3, 4])) == {2, 3}

def test_find_mode_empty_list():
    """Test handling of empty list"""
    assert find_mode([]) is None

def test_find_mode_all_unique():
    """Test list with all unique elements"""
    assert find_mode([1, 2, 3, 4, 5]) == 1

def test_find_mode_type_error():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_mode("not a list")
        find_mode(123)
        find_mode(None)
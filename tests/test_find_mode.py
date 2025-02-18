import pytest
from src.find_mode import find_mode

def test_single_mode():
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    result = find_mode([1, 1, 2, 2, 3])
    assert set(result) == {1, 2}

def test_all_unique_elements():
    result = find_mode([1, 2, 3, 4, 5])
    assert set(result) == {1, 2, 3, 4, 5}

def test_float_numbers():
    assert find_mode([1.5, 2.5, 2.5, 3.5]) == 2.5

def test_mixed_types():
    result = find_mode([1, 1, 2, 2.0, 3])
    assert result == 1

def test_empty_list():
    with pytest.raises(ValueError, match="Cannot find mode of an empty list"):
        find_mode([])
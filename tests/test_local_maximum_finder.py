import pytest
from src.local_maximum_finder import find_local_maxima

def test_basic_local_maxima():
    arr = [1, 3, 2, 4, 1, 5, 3]
    assert find_local_maxima(arr) == [1, 3, 5]

def test_single_element():
    arr = [42]
    assert find_local_maxima(arr) == [0]

def test_ascending_array():
    arr = [1, 2, 3, 4, 5]
    assert find_local_maxima(arr) == [4]

def test_descending_array():
    arr = [5, 4, 3, 2, 1]
    assert find_local_maxima(arr) == [0]

def test_array_with_duplicates():
    arr = [1, 2, 2, 3, 3, 2, 1]
    assert find_local_maxima(arr) == [3]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_local_maxima("not a list")

def test_empty_list():
    with pytest.raises(ValueError):
        find_local_maxima([])
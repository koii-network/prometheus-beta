import pytest
from src.suffix_array import create_suffix_array, search_suffix_array

def test_create_suffix_array_basic():
    s = "banana"
    suffix_arr = create_suffix_array(s)
    # Expected suffix array for "banana": [5, 3, 1, 0, 4, 2]
    assert suffix_arr == [5, 3, 1, 0, 4, 2]

def test_create_suffix_array_empty_string():
    s = ""
    suffix_arr = create_suffix_array(s)
    assert suffix_arr == []

def test_create_suffix_array_single_char():
    s = "a"
    suffix_arr = create_suffix_array(s)
    assert suffix_arr == [0]

def test_create_suffix_array_invalid_input():
    with pytest.raises(TypeError):
        create_suffix_array(123)
    with pytest.raises(TypeError):
        create_suffix_array(None)

def test_search_suffix_array_basic():
    s = "banana"
    suffix_arr = create_suffix_array(s)
    
    # Test pattern that exists
    assert search_suffix_array(suffix_arr, s, "ana") == [1, 3]
    assert search_suffix_array(suffix_arr, s, "ban") == [3]
    assert search_suffix_array(suffix_arr, s, "a") == [1, 3, 5]

def test_search_suffix_array_not_found():
    s = "banana"
    suffix_arr = create_suffix_array(s)
    
    # Test pattern that doesn't exist
    assert search_suffix_array(suffix_arr, s, "xyz") == []

def test_search_suffix_array_edge_cases():
    s = "banana"
    suffix_arr = create_suffix_array(s)
    
    # Empty pattern
    assert search_suffix_array(suffix_arr, s, "") == []
    
    # Pattern longer than string
    with pytest.raises(ValueError):
        search_suffix_array(suffix_arr, s, "bananas")

def test_search_suffix_array_invalid_inputs():
    s = "banana"
    suffix_arr = create_suffix_array(s)
    
    with pytest.raises(TypeError):
        search_suffix_array(None, s, "ana")
    with pytest.raises(TypeError):
        search_suffix_array(suffix_arr, 123, "ana")
    with pytest.raises(TypeError):
        search_suffix_array(suffix_arr, s, 123)
import pytest
from src.list_flattener import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a simple list"""
    input_list = [1, 2, 3]
    assert flatten_nested_list(input_list) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a list with one level of nesting"""
    input_list = [1, [2, 3], 4]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4]

def test_flatten_deep_nested_list():
    """Test flattening a deeply nested list"""
    input_list = [1, [2, [3, 4]], [5, [6, 7]]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types"""
    input_list = [1, 'a', [2, 'b', [3, 'c']]]
    assert flatten_nested_list(input_list) == [1, 'a', 2, 'b', 3, 'c']

def test_flatten_empty_list():
    """Test flattening an empty list"""
    input_list = []
    assert flatten_nested_list(input_list) == []

def test_flatten_no_nesting():
    """Test flattening a list with no nesting"""
    input_list = [1, 2, 3, 4, 5]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list(None)
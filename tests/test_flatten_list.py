import pytest
from src.flatten_list import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a simple list"""
    input_list = [1, 2, 3, 4, 5]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5]

def test_flatten_nested_list():
    """Test flattening a list with nested lists"""
    input_list = [1, [2, 3], [4, [5, 6]], 7]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    input_list = [1, [2, [3, [4]]], [5, 6]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types"""
    input_list = [1, 'a', [2, 3.14], [['hello'], [4, 5]]]
    assert flatten_nested_list(input_list) == [1, 'a', 2, 3.14, 'hello', 4, 5]

def test_empty_list():
    """Test flattening an empty list"""
    input_list = []
    assert flatten_nested_list(input_list) == []

def test_no_nested_lists():
    """Test that a list without nested lists is not modified"""
    input_list = [1, 2, 3]
    assert flatten_nested_list(input_list) == [1, 2, 3]

def test_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list(None)
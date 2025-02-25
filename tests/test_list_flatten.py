import pytest
from src.list_flatten import flatten_list

def test_flatten_simple_list():
    """Test flattening a simple list"""
    input_list = [1, 2, 3]
    assert flatten_list(input_list) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list"""
    input_list = [1, [2, 3], 4]
    assert flatten_list(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    input_list = [1, [2, [3, 4]], 5, [6, [7, 8]]]
    assert flatten_list(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    input_list = []
    assert flatten_list(input_list) == []

def test_flatten_list_with_empty_nested_lists():
    """Test flattening a list with empty nested lists"""
    input_list = [1, [], [2, []], 3]
    assert flatten_list(input_list) == [1, 2, 3]

def test_unsupported_type_raises_error():
    """Test that unsupported types raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_list([1, 2, "3"])
    
    with pytest.raises(TypeError):
        flatten_list([1, [2, 3.5], 4])
import pytest
from src.list_utils import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a simple non-nested list."""
    input_list = [1, 2, 3, 4, 5]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5]

def test_flatten_nested_list():
    """Test flattening a list with one level of nesting."""
    input_list = [1, [2, 3], 4, [5, 6]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_list():
    """Test flattening a list with multiple levels of nesting."""
    input_list = [1, [2, [3, 4]], [5, [6, 7]], 8]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    input_list = []
    assert flatten_nested_list(input_list) == []

def test_flatten_mixed_types():
    """Test flattening a list with mixed types."""
    input_list = [1, 'a', [2, 'b'], [3.14, [True, False]]]
    assert flatten_nested_list(input_list) == [1, 'a', 2, 'b', 3.14, True, False]

def test_flatten_non_list_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError):
        flatten_nested_list("not a list")
    
    with pytest.raises(TypeError):
        flatten_nested_list(42)
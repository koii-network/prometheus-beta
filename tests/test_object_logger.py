import pytest
import json
from src.object_logger import log_object

def test_log_object_dict():
    """Test logging a simple dictionary."""
    test_dict = {"name": "John", "age": 30}
    logged = log_object(test_dict)
    assert json.loads(logged) == test_dict

def test_log_object_list():
    """Test logging a list."""
    test_list = [1, 2, 3, 4, 5]
    logged = log_object(test_list)
    assert json.loads(logged) == test_list

def test_log_object_nested():
    """Test logging a nested dictionary."""
    test_nested = {"user": {"name": "Alice", "details": {"age": 25, "city": "New York"}}}
    logged = log_object(test_nested)
    assert json.loads(logged) == test_nested

def test_log_object_sorted_keys():
    """Test logging with sorted keys."""
    test_dict = {"z": 1, "a": 2, "m": 3}
    logged = log_object(test_dict, sort_keys=True)
    # When sorted, keys should be in alphabetical order
    assert list(json.loads(logged).keys()) == ["a", "m", "z"]

def test_log_object_compact():
    """Test compact logging."""
    test_dict = {"name": "John", "age": 30}
    logged = log_object(test_dict, compact=True)
    # Compact mode should remove whitespace
    assert logged == '{"name":"John","age":30}'

def test_log_object_custom_indent():
    """Test custom indentation."""
    test_dict = {"name": "John"}
    logged = log_object(test_dict, indent=4)
    # Check if the output uses 4-space indentation
    assert logged.count(' ') > 0  # Ensure there's indentation
    assert logged.startswith('{\n    ')

def test_log_object_complex_object():
    """Test logging a complex object that requires pprint."""
    class ComplexObject:
        def __init__(self):
            self.data = "sample"
    
    obj = ComplexObject()
    logged = log_object(obj)
    assert "data" in logged
    assert "'sample'" in logged

def test_log_object_none():
    """Test logging None."""
    logged = log_object(None)
    assert logged == "null"
import pytest
from object_logger import log_object

def test_log_simple_dict():
    test_dict = {"name": "John", "age": 30}
    result = log_object(test_dict)
    assert "John" in result
    assert "30" in result

def test_log_nested_dict():
    test_dict = {
        "name": "Alice", 
        "details": {
            "age": 25, 
            "city": "New York"
        }
    }
    result = log_object(test_dict)
    assert "Alice" in result
    assert "New York" in result

def test_log_list():
    test_list = [1, 2, 3, {"a": 1}]
    result = log_object(test_list)
    assert "1" in result
    assert "2" in result
    assert "3" in result

def test_log_max_depth():
    deep_dict = {
        "a": {
            "b": {
                "c": {
                    "d": "too deep"
                }
            }
        }
    }
    # Should only show partial depth
    result = log_object(deep_dict, max_depth=2)
    assert "too deep" not in result

def test_log_unserializable_object():
    class UnserializableClass:
        def __init__(self):
            self.x = 1
    
    result = log_object(UnserializableClass())
    assert "Unable to log object" in result
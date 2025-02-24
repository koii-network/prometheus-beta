import json
import pytest
from src.object_logger import log_object

class TestObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def test_log_none():
    assert log_object(None) == "None"

def test_log_primitive_types():
    assert log_object(42) == "42"
    assert log_object(3.14) == "3.14"
    assert log_object("hello") == "hello"
    assert log_object(True) == "True"
    assert log_object(False) == "False"

def test_log_dictionary():
    test_dict = {"key1": "value1", "key2": 42}
    logged_dict = log_object(test_dict)
    assert json.loads(logged_dict) == test_dict

def test_log_list():
    test_list = [1, 2, 3, "four"]
    logged_list = log_object(test_list)
    assert json.loads(logged_list) == test_list

def test_log_tuple():
    test_tuple = (1, 2, 3, "four")
    logged_tuple = log_object(test_tuple)
    assert json.loads(logged_tuple) == list(test_tuple)

def test_log_set():
    test_set = {1, 2, 3, "four"}
    logged_set = log_object(test_set)
    assert set(json.loads(logged_set)) == test_set

def test_log_custom_object():
    test_obj = TestObject("test", 123)
    logged_obj = log_object(test_obj)
    parsed_obj = json.loads(logged_obj)
    assert parsed_obj == {"name": "test", "value": 123}

def test_custom_indent():
    test_dict = {"key1": "value1", "key2": 42}
    logged_dict = log_object(test_dict, indent=4)
    # Verify that the logged output uses 4-space indentation
    assert logged_dict.count('\n') > 1  # Multiple lines
    assert '    ' in logged_dict  # 4-space indentation

def test_unsupported_object_type():
    class UnlogableObject:
        pass
    
    with pytest.raises(TypeError):
        log_object(UnlogableObject())
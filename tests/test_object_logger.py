import pytest
from src.object_logger import log_object

def test_log_simple_dict():
    test_dict = {"name": "John", "age": 30}
    result = log_object(test_dict)
    assert "John" in result
    assert "30" in result
    assert "{" in result
    assert "}" in result

def test_log_nested_dict():
    test_dict = {
        "user": {
            "name": "Alice", 
            "details": {
                "age": 25, 
                "city": "New York"
            }
        }
    }
    result = log_object(test_dict)
    assert "Alice" in result
    assert "New York" in result
    assert "25" in result

def test_log_list():
    test_list = [1, 2, 3, {"key": "value"}]
    result = log_object(test_list)
    assert "1" in result
    assert "2" in result
    assert "3" in result
    assert "value" in result

def test_log_custom_indent():
    test_dict = {"name": "Bob", "age": 35}
    result = log_object(test_dict, indent=4)
    result_lines = result.split('\n')
    assert len(result_lines) > 1  # Ensure multiple lines
    assert '    ' in result  # Ensure 4-space indentation is used

def test_log_non_serializable_object():
    class CustomObject:
        def __init__(self):
            self.value = "custom"
    
    obj = CustomObject()
    result = log_object(obj)
    assert isinstance(result, str)
    assert "custom" in result or "object" in result.lower()
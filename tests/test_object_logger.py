import pytest
import logging
from src.object_logger import log_object_details

class TestClass:
    def __init__(self):
        self.name = "Test Object"
        self.value = 42

def test_log_dictionary():
    """Test logging a dictionary"""
    test_dict = {"key1": "value1", "key2": 42}
    result = log_object_details(test_dict)
    assert result == test_dict

def test_log_object_with_dict():
    """Test logging an object with __dict__"""
    test_obj = TestClass()
    result = log_object_details(test_obj)
    assert result == {"name": "Test Object", "value": 42}

def test_log_object_invalid_type():
    """Test logging an object that cannot be converted to a dictionary"""
    with pytest.raises(TypeError):
        log_object_details(42)

def test_log_object_with_to_dict_method():
    """Test logging an object with a to_dict method"""
    class CustomObject:
        def __init__(self):
            self.x = 1
            self.y = 2
        
        def to_dict(self):
            return {"x": self.x, "y": self.y}
    
    test_obj = CustomObject()
    result = log_object_details(test_obj)
    assert result == {"x": 1, "y": 2}
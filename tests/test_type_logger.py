import pytest
import logging
from src.type_logger import log_variable_type

def test_log_variable_type(caplog):
    # Test integer
    caplog.set_level(logging.INFO)
    result = log_variable_type(42)
    assert result == 'int'
    assert "Variable type: int" in caplog.text

    # Test string
    caplog.clear()
    result = log_variable_type("Hello")
    assert result == 'str'
    assert "Variable type: str" in caplog.text

    # Test list
    caplog.clear()
    result = log_variable_type([1, 2, 3])
    assert result == 'list'
    assert "Variable type: list" in caplog.text

    # Test dictionary
    caplog.clear()
    result = log_variable_type({"key": "value"})
    assert result == 'dict'
    assert "Variable type: dict" in caplog.text

    # Test None
    caplog.clear()
    result = log_variable_type(None)
    assert result == 'NoneType'
    assert "Variable type: NoneType" in caplog.text

    # Test custom class
    class CustomClass:
        pass
    
    caplog.clear()
    custom_obj = CustomClass()
    result = log_variable_type(custom_obj)
    assert result == 'CustomClass'
    assert "Variable type: CustomClass" in caplog.text
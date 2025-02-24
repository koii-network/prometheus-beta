import logging
import pytest
from src.variable_type_logger import log_variable_type

def test_log_string_type(caplog):
    """Test logging type of a string."""
    caplog.set_level(logging.INFO)
    result = log_variable_type("hello")
    assert result == str
    assert "Variable type: str" in caplog.text

def test_log_int_type(caplog):
    """Test logging type of an integer."""
    caplog.set_level(logging.INFO)
    result = log_variable_type(42)
    assert result == int
    assert "Variable type: int" in caplog.text

def test_log_float_type(caplog):
    """Test logging type of a float."""
    caplog.set_level(logging.INFO)
    result = log_variable_type(3.14)
    assert result == float
    assert "Variable type: float" in caplog.text

def test_log_list_type(caplog):
    """Test logging type of a list."""
    caplog.set_level(logging.INFO)
    result = log_variable_type([1, 2, 3])
    assert result == list
    assert "Variable type: list" in caplog.text

def test_log_dict_type(caplog):
    """Test logging type of a dictionary."""
    caplog.set_level(logging.INFO)
    result = log_variable_type({"key": "value"})
    assert result == dict
    assert "Variable type: dict" in caplog.text

def test_log_tuple_type(caplog):
    """Test logging type of a tuple."""
    caplog.set_level(logging.INFO)
    result = log_variable_type((1, 2, 3))
    assert result == tuple
    assert "Variable type: tuple" in caplog.text

def test_log_none_type():
    """Test that None raises a TypeError."""
    with pytest.raises(TypeError, match="Input variable cannot be None"):
        log_variable_type(None)
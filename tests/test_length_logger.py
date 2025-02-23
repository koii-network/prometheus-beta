import pytest
import logging
from src.length_logger import log_length

def test_log_length_string(caplog):
    """Test logging length of a string"""
    caplog.set_level(logging.INFO)
    result = log_length("hello")
    assert result == 5
    assert "Length of item: 5" in caplog.text

def test_log_length_list(caplog):
    """Test logging length of a list"""
    caplog.set_level(logging.INFO)
    result = log_length([1, 2, 3, 4])
    assert result == 4
    assert "Length of item: 4" in caplog.text

def test_log_length_empty_string(caplog):
    """Test logging length of an empty string"""
    caplog.set_level(logging.INFO)
    result = log_length("")
    assert result == 0
    assert "Length of item: 0" in caplog.text

def test_log_length_empty_list(caplog):
    """Test logging length of an empty list"""
    caplog.set_level(logging.INFO)
    result = log_length([])
    assert result == 0
    assert "Length of item: 0" in caplog.text

def test_log_length_invalid_type():
    """Test raising TypeError for invalid input type"""
    with pytest.raises(TypeError, match="Input must be a string or list"):
        log_length(123)
    
    with pytest.raises(TypeError, match="Input must be a string or list"):
        log_length(None)
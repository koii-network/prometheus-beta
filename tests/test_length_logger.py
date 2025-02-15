import pytest
import logging
from src.length_logger import log_length

def test_log_length_string(caplog):
    caplog.set_level(logging.INFO)
    result = log_length("hello")
    assert result == 5
    assert "Length of input: 5" in caplog.text

def test_log_length_list(caplog):
    caplog.set_level(logging.INFO)
    result = log_length([1, 2, 3, 4])
    assert result == 4
    assert "Length of input: 4" in caplog.text

def test_log_length_empty_string(caplog):
    caplog.set_level(logging.INFO)
    result = log_length("")
    assert result == 0
    assert "Length of input: 0" in caplog.text

def test_log_length_empty_list(caplog):
    caplog.set_level(logging.INFO)
    result = log_length([])
    assert result == 0
    assert "Length of input: 0" in caplog.text

def test_log_length_invalid_type():
    with pytest.raises(TypeError, match="Input must be a string or list/array"):
        log_length(123)
    
    with pytest.raises(TypeError, match="Input must be a string or list/array"):
        log_length(None)
import pytest
import logging
from src.length_logger import log_length

def test_log_length_string():
    # Test logging length of a string
    logging.basicConfig(level=logging.INFO)
    
    # Capture log messages
    with pytest.caplog.at_level(logging.INFO):
        result = log_length("hello")
        assert result == 5
        assert "Length of item: 5" in caplog.text

def test_log_length_list():
    # Test logging length of a list
    logging.basicConfig(level=logging.INFO)
    
    with pytest.caplog.at_level(logging.INFO):
        result = log_length([1, 2, 3, 4])
        assert result == 4
        assert "Length of item: 4" in caplog.text

def test_log_length_tuple():
    # Test logging length of a tuple
    logging.basicConfig(level=logging.INFO)
    
    with pytest.caplog.at_level(logging.INFO):
        result = log_length((1, 2))
        assert result == 2
        assert "Length of item: 2" in caplog.text

def test_log_length_invalid_type():
    # Test raising TypeError for invalid input type
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length(123)

def test_log_length_empty():
    # Test empty string, list, and tuple
    logging.basicConfig(level=logging.INFO)
    
    with pytest.caplog.at_level(logging.INFO):
        assert log_length("") == 0
        assert log_length([]) == 0
        assert log_length(()) == 0
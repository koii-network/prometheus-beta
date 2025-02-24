import logging
import pytest
from io import StringIO
import sys

from src.object_logger import log_object_details

def test_log_dictionary(caplog):
    """Test logging a dictionary"""
    test_dict = {"name": "John", "age": 30, "city": "New York"}
    
    # Capture log messages
    caplog.set_level(logging.INFO)
    log_object_details(test_dict)
    
    # Check log contents
    log_records = caplog.records
    assert len(log_records) == 4  # Header + 3 entries
    assert "Dictionary with 3 entries" in log_records[0].message
    assert "'name'" in log_records[1].message
    assert "'age'" in log_records[2].message
    assert "'city'" in log_records[3].message

def test_log_list(caplog):
    """Test logging a list"""
    test_list = [1, "two", 3.0, [4, 5]]
    
    # Capture log messages
    caplog.set_level(logging.INFO)
    log_object_details(test_list)
    
    # Check log contents
    log_records = caplog.records
    assert len(log_records) == 5  # Header + 4 entries
    assert "List with 4 entries" in log_records[0].message
    assert all(str(i) in log_records[i+1].message for i in range(4))

def test_log_non_dict_list_object(caplog):
    """Test logging a non-dictionary/list object"""
    test_obj = 42
    
    # Capture log messages
    caplog.set_level(logging.INFO)
    log_object_details(test_obj)
    
    # Check log contents
    log_records = caplog.records
    assert len(log_records) == 1
    assert "int" in log_records[0].message
    assert "42" in log_records[0].message

def test_log_with_custom_log_level(caplog):
    """Test logging with a custom log level"""
    test_dict = {"key": "value"}
    
    # Capture log messages with DEBUG level
    caplog.set_level(logging.DEBUG)
    log_object_details(test_dict, log_level=logging.DEBUG)
    
    # Check log contents
    log_records = caplog.records
    assert len(log_records) == 4
    assert log_records[0].levelno == logging.DEBUG
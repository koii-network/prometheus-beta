import pytest
import logging
from src.object_logger import log_object_details

def test_log_object_details(caplog):
    # Test basic logging functionality
    test_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    caplog.set_level(logging.INFO)
    
    result = log_object_details(test_dict)
    
    # Check return value
    assert result == 3
    
    # Check log messages
    log_records = caplog.records
    assert len(log_records) == 4  # 1 initial message + 3 key-value messages
    assert "Logging object details:" in log_records[0].message
    assert "Key: name, Value: John" in [record.message for record in log_records]
    assert "Key: age, Value: 30" in [record.message for record in log_records]
    assert "Key: city, Value: New York" in [record.message for record in log_records]

def test_log_object_details_empty_dict(caplog):
    # Test logging an empty dictionary
    caplog.set_level(logging.INFO)
    
    result = log_object_details({})
    
    assert result == 0
    log_records = caplog.records
    assert len(log_records) == 1
    assert "Logging object details:" in log_records[0].message

def test_log_object_details_invalid_input():
    # Test that TypeError is raised for non-dictionary input
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details("not a dict")
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(123)
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(None)
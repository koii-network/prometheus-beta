import pytest
import logging
import json
from src.object_logger import log_object

class MockLogger:
    def __init__(self):
        self.logged_messages = []
        
    def debug(self, msg):
        self.logged_messages.append(('debug', msg))
    
    def info(self, msg):
        self.logged_messages.append(('info', msg))
    
    def warning(self, msg):
        self.logged_messages.append(('warning', msg))
    
    def error(self, msg):
        self.logged_messages.append(('error', msg))
    
    def critical(self, msg):
        self.logged_messages.append(('critical', msg))

def test_log_object_dict():
    mock_logger = MockLogger()
    test_dict = {'name': 'John', 'age': 30}
    
    result = log_object(test_dict, logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_messages[0][0] == 'info'
    assert json.loads(result) == test_dict

def test_log_object_custom_log_level():
    mock_logger = MockLogger()
    test_obj = [1, 2, 3]
    
    result = log_object(test_obj, log_level='warning', logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_messages[0][0] == 'warning'
    assert json.loads(result) == test_obj

def test_log_object_complex_object():
    mock_logger = MockLogger()
    test_obj = {
        'name': 'Complex Object',
        'nested': {'a': 1, 'b': [1, 2, 3]},
        'datetime': pytest.lazy_fixture('mock_datetime')
    }
    
    result = log_object(test_obj, logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_messages[0][0] == 'info'

def test_invalid_log_level():
    with pytest.raises(ValueError, match="Invalid log level"):
        log_object({'key': 'value'}, log_level='invalid')

def test_non_json_serializable_object():
    class NonSerializable:
        def __str__(self):
            return "Custom Object"
    
    mock_logger = MockLogger()
    obj = NonSerializable()
    
    result = log_object(obj, logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert result == str(obj)
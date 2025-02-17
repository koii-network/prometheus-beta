import logging
import pytest
from src.parameter_logger import log_params

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.log_messages = []
    
    def info(self, message):
        self.log_messages.append(message)

@log_params()
def sample_function(a, b, c=10):
    return a + b + c

@log_params()
def function_with_default_args(x, y=5, z=None):
    return x * y

def test_log_params_with_default_args():
    mock_logger = MockLogger()
    
    with pytest.MonkeyPatch.context() as m:
        m.setattr(logging, 'getLogger', lambda: mock_logger)
        result = function_with_default_args(3)
        
        # Check log messages
        assert len(mock_logger.log_messages) == 3
        assert "Calling function: function_with_default_args" in mock_logger.log_messages[0]
        assert "Parameter 'x': 3" in mock_logger.log_messages[1]
        assert "Parameter 'y': 5" in mock_logger.log_messages[2]
        
        # Check function result
        assert result == 15

def test_log_params_with_all_args():
    mock_logger = MockLogger()
    
    with pytest.MonkeyPatch.context() as m:
        m.setattr(logging, 'getLogger', lambda: mock_logger)
        result = sample_function(1, 2, 3)
        
        # Check log messages
        assert len(mock_logger.log_messages) == 3
        assert "Calling function: sample_function" in mock_logger.log_messages[0]
        assert "Parameter 'a': 1" in mock_logger.log_messages[1]
        assert "Parameter 'b': 2" in mock_logger.log_messages[2]
        assert "Parameter 'c': 3" in mock_logger.log_messages[2]
        
        # Check function result
        assert result == 6

def test_log_params_with_kwargs():
    mock_logger = MockLogger()
    
    with pytest.MonkeyPatch.context() as m:
        m.setattr(logging, 'getLogger', lambda: mock_logger)
        result = sample_function(1, b=2, c=3)
        
        # Check log messages
        assert len(mock_logger.log_messages) == 3
        assert "Calling function: sample_function" in mock_logger.log_messages[0]
        assert "Parameter 'a': 1" in mock_logger.log_messages[1]
        assert "Parameter 'b': 2" in mock_logger.log_messages[2]
        assert "Parameter 'c': 3" in mock_logger.log_messages[2]
        
        # Check function result
        assert result == 6
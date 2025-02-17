import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

class TestReadlineLogger:
    @pytest.fixture
    def capture_logs(self):
        """
        Fixture to capture log output for testing.
        """
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        
        yield log_capture
        
        logger.removeHandler(handler)
        log_capture.close()
    
    def test_initialization(self):
        """
        Test logger initialization.
        """
        logger = ReadlineLogger()
        assert logger.logger is not None
    
    def test_start_and_stop_logging(self, capture_logs):
        """
        Test starting and stopping logging hooks.
        """
        logger = ReadlineLogger()
        logger.start_logging()
        assert logger._original_hook is not None
        
        logger.stop_logging()
        assert logger._original_hook is None
    
    def test_log_input(self, capture_logs):
        """
        Test logging input with a custom message.
        """
        logger = ReadlineLogger()
        
        with patch('builtins.input', return_value='test response'):
            response = logger.log_input("Enter something: ", "Custom log message")
        
        log_output = capture_logs.getvalue()
        assert "Custom log message" in log_output
        assert response == 'test response'
    
    def test_stop_logging_without_active_hook(self, capture_logs):
        """
        Test stopping logging when no hook is active.
        """
        logger = ReadlineLogger()
        logger.stop_logging()
        
        log_output = capture_logs.getvalue()
        assert "No active logging hook to stop" in log_output
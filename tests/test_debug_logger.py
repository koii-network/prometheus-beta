import os
import logging
import pytest
from src.debug_logger import conditional_debug_log

class TestConditionalDebugLog:
    def setup_method(self):
        # Reset environment variable before each test
        if 'DEBUG' in os.environ:
            del os.environ['DEBUG']
        
        # Create a logger for testing
        self.test_logger = logging.getLogger('test_logger')
        self.test_logger.setLevel(logging.DEBUG)
        
        # Create a handler to capture log messages
        self.log_capture = []
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.emit = lambda record: self.log_capture.append(handler.format(record))
        self.test_logger.addHandler(handler)
    
    def test_default_no_logging(self):
        """Test that no logging occurs by default"""
        result = conditional_debug_log("Test message", logger=self.test_logger)
        assert result is False
        assert len(self.log_capture) == 0
    
    def test_explicit_condition_true(self):
        """Test logging when condition is explicitly True"""
        result = conditional_debug_log("Explicit message", condition=True, logger=self.test_logger)
        assert result is True
        assert len(self.log_capture) == 1
        assert "Explicit message" in self.log_capture[0]
    
    def test_explicit_condition_false(self):
        """Test no logging when condition is explicitly False"""
        result = conditional_debug_log("Suppressed message", condition=False, logger=self.test_logger)
        assert result is False
        assert len(self.log_capture) == 0
    
    def test_debug_env_var_true(self):
        """Test logging when DEBUG env var is set to true"""
        os.environ['DEBUG'] = 'true'
        result = conditional_debug_log("Environment message", logger=self.test_logger)
        assert result is True
        assert len(self.log_capture) == 1
        assert "Environment message" in self.log_capture[0]
    
    def test_debug_env_var_false(self):
        """Test no logging when DEBUG env var is not set"""
        os.environ['DEBUG'] = '0'
        result = conditional_debug_log("Ignored message", logger=self.test_logger)
        assert result is False
        assert len(self.log_capture) == 0
    
    def test_message_type(self):
        """Test that non-string messages are converted to strings"""
        result = conditional_debug_log(42, condition=True, logger=self.test_logger)
        assert result is True
        assert len(self.log_capture) == 1
        assert "42" in self.log_capture[0]
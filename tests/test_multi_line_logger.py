import logging
import pytest
from io import StringIO
import sys

from src.multi_line_logger import log_multiline

class TestMultiLineLogger:
    @pytest.fixture
    def caplog(self):
        """Capture log output for testing"""
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        
        # Create a StringIO to capture log output
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        logger.addHandler(handler)
        
        yield log_capture
        
        # Remove the handler after test
        logger.removeHandler(handler)
        log_capture.close()
    
    def test_default_logging(self, caplog):
        """Test default logging behavior"""
        log_multiline("Test message")
        log_output = caplog.getvalue()
        
        assert "Test message" in log_output
        assert log_output.count('=') == 80  # 2 lines of 40 '=' each
    
    def test_custom_separator(self, caplog):
        """Test custom separator"""
        log_multiline("Custom sep", separator='-', separator_length=20)
        log_output = caplog.getvalue()
        
        assert "Custom sep" in log_output
        assert log_output.count('-') == 40  # 2 lines of 20 '-'
    
    def test_different_log_levels(self, caplog):
        """Test different logging levels"""
        log_levels = [
            logging.DEBUG, 
            logging.INFO, 
            logging.WARNING, 
            logging.ERROR, 
            logging.CRITICAL
        ]
        
        for level in log_levels:
            caplog.truncate(0)  # Clear previous log
            caplog.seek(0)
            
            log_multiline(f"Level {level} message", level=level)
            log_output = caplog.getvalue()
            
            assert f"Level {level} message" in log_output
    
    def test_multiline_message(self, caplog):
        """Test multiline message logging"""
        multiline_msg = "Line 1\nLine 2\nLine 3"
        log_multiline(multiline_msg)
        log_output = caplog.getvalue()
        
        assert "Line 1" in log_output
        assert "Line 2" in log_output
        assert "Line 3" in log_output
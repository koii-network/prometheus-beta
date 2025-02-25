import pytest
import logging
import time
from unittest.mock import Mock, patch
from src.process_progress_logger import ProcessProgressLogger, track_process

class TestProcessProgressLogger:
    def setup_method(self):
        # Reset logging to capture log messages
        logging.getLogger().handlers = []
        logging.getLogger().setLevel(logging.DEBUG)
    
    def test_initialization(self):
        logger = Mock(spec=logging.Logger)
        progress_logger = ProcessProgressLogger(total_steps=10, logger=logger)
        
        assert progress_logger.total_steps == 10
        assert progress_logger.current_step == 0
        assert progress_logger.logger == logger
    
    def test_invalid_initialization(self):
        with pytest.raises(ValueError, match="total_steps must be a positive integer"):
            ProcessProgressLogger(total_steps=0)
        
        with pytest.raises(ValueError, match="total_steps must be a positive integer"):
            ProcessProgressLogger(total_steps=-5)
    
    def test_update_progress(self):
        mock_logger = Mock(spec=logging.Logger)
        progress_logger = ProcessProgressLogger(total_steps=5, logger=mock_logger)
        
        progress_logger.update()  # Default 1 step
        assert progress_logger.current_step == 1
        mock_logger.log.assert_called_once()
        
        progress_logger.update(steps=2)
        assert progress_logger.current_step == 3
    
    def test_update_progress_exceed_steps(self):
        progress_logger = ProcessProgressLogger(total_steps=5)
        
        with pytest.raises(ValueError, match="Cannot progress beyond total steps"):
            progress_logger.update(steps=6)
    
    def test_complete_method(self):
        mock_logger = Mock(spec=logging.Logger)
        progress_logger = ProcessProgressLogger(total_steps=5, logger=mock_logger)
        
        progress_logger.update(steps=3)
        progress_logger.complete()
        
        assert progress_logger.current_step == 5
        mock_logger.log.assert_called()
    
    def test_track_process_decorator(self):
        # Mock logger and process
        mock_logger = Mock(spec=logging.Logger)
        
        @track_process(total_steps=3, logger=mock_logger)
        def sample_process():
            time.sleep(0.1)  # Simulate work
            return "Success"
        
        result = sample_process()
        
        assert result == "Success"
        mock_logger.log.assert_called()
        mock_logger.error.assert_not_called()
    
    def test_track_process_decorator_with_error(self):
        # Mock logger and process that raises an error
        mock_logger = Mock(spec=logging.Logger)
        
        @track_process(total_steps=3, logger=mock_logger)
        def failing_process():
            raise ValueError("Test error")
        
        with pytest.raises(ValueError, match="Test error"):
            failing_process()
        
        mock_logger.error.assert_called_once()
    
    def test_log_message_content(self):
        # Capture log messages to verify their content
        log_capture = []
        
        class CaptureHandler(logging.Handler):
            def emit(self, record):
                log_capture.append(record)
        
        logger = logging.getLogger(__name__)
        capture_handler = CaptureHandler()
        logger.addHandler(capture_handler)
        logger.setLevel(logging.INFO)
        
        # Log a progress update
        progress_logger = ProcessProgressLogger(total_steps=10, logger=logger)
        progress_logger.update(steps=3)
        
        # Verify log message contains expected information
        assert len(log_capture) > 0
        log_message = log_capture[0].getMessage()
        assert "Progress:" in log_message
        assert "30.00%" in log_message
        assert "Estimated time remaining:" in log_message
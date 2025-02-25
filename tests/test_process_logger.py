import pytest
import logging
import time
from io import StringIO
from src.process_logger import ProcessLogger

class TestProcessLogger:
    def setup_method(self):
        """Setup method to create a fresh logger for each test"""
        # Capture log output
        self.log_capture = StringIO()
        handler = logging.StreamHandler(self.log_capture)
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        
        # Create ProcessLogger with test logger
        self.process_logger = ProcessLogger(logger=self.logger)
    
    def test_log_progress_basic(self):
        """Test basic progress logging"""
        for i in range(0, 101, 10):
            self.process_logger.log_progress(i, 100)
        
        log_output = self.log_capture.getvalue()
        assert "Progress: 0/100 (0.00%)" in log_output
        assert "Progress: 100/100 (100.00%)" in log_output
    
    def test_log_progress_custom_frequency(self):
        """Test logging with custom frequency"""
        for i in range(0, 101, 20):
            self.process_logger.log_progress(i, 100, frequency=20)
        
        log_output = self.log_capture.getvalue()
        assert "Progress: 0/100 (0.00%)" in log_output
        assert "Progress: 100/100 (100.00%)" in log_output
        # Ensure not every iteration is logged
        assert log_output.count("Progress:") <= 6
    
    def test_log_progress_with_message(self):
        """Test logging with custom message"""
        self.process_logger.log_progress(50, 100, message="Halfway there")
        
        log_output = self.log_capture.getvalue()
        assert "Progress: 50/100 (50.00%)" in log_output
        assert "Halfway there" in log_output
    
    def test_invalid_progress_inputs(self):
        """Test error handling for invalid inputs"""
        with pytest.raises(ValueError, match="Total must be a positive number"):
            self.process_logger.log_progress(50, 0)
        
        with pytest.raises(ValueError, match="Current progress cannot be negative"):
            self.process_logger.log_progress(-10, 100)
        
        with pytest.raises(ValueError, match="Current progress cannot exceed total"):
            self.process_logger.log_progress(110, 100)
    
    def test_track_process_success(self):
        """Test tracking a successful process"""
        def sample_process(x, y):
            return x + y
        
        result = self.process_logger.track_process(sample_process, 3, 4)
        assert result == 7
        
        log_output = self.log_capture.getvalue()
        assert "Process failed" not in log_output
    
    def test_track_process_failure(self):
        """Test tracking a failed process"""
        def failing_process():
            raise RuntimeError("Process failed")
        
        with pytest.raises(RuntimeError, match="Process failed"):
            self.process_logger.track_process(failing_process)
        
        log_output = self.log_capture.getvalue()
        assert "Process failed" in log_output
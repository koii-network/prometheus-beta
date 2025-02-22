import pytest
import time
from src.frame_rate_logger import FrameRateLogger

class TestFrameRateLogger:
    def test_initialization(self):
        """Test logger initialization."""
        logger = FrameRateLogger()
        assert logger.log_interval == 1000
        assert logger.frames_rendered == 0
        assert logger.logs == []
    
    def test_start(self):
        """Test start method."""
        logger = FrameRateLogger()
        logger.start()
        assert logger.start_time is not None
        assert logger.frames_rendered == 0
    
    def test_log_frame(self):
        """Test logging frames."""
        logger = FrameRateLogger(log_interval=100)
        logger.start()
        
        # Override _get_current_time for predictable testing
        def mock_time():
            mock_time.current += 50
            return mock_time.current
        mock_time.current = 0
        logger._get_current_time = mock_time
        
        # Log multiple frames
        logger.log_frame()
        logger.log_frame()
        logger.log_frame()
        
        # Log after interval
        mock_time.current += 100
        logger.log_frame()
        
        # Check logs
        logs = logger.get_logs()
        assert len(logs) == 1
        log_entry = logs[0]
        assert 'timestamp' in log_entry
        assert 'frames_rendered' in log_entry
        assert 'fps' in log_entry
        assert log_entry['frames_rendered'] == 3
    
    def test_get_logs(self):
        """Test retrieving logs."""
        logger = FrameRateLogger(log_interval=200)
        logger.start()
        
        # Override _get_current_time for predictable testing
        def mock_time():
            mock_time.current += 250
            return mock_time.current
        mock_time.current = 0
        logger._get_current_time = mock_time
        
        logger.log_frame()
        logger.log_frame()
        mock_time.current += 250
        logger.log_frame()
        
        logs = logger.get_logs()
        assert len(logs) == 2
    
    def test_custom_log_interval(self):
        """Test custom log interval."""
        logger = FrameRateLogger(log_interval=500)
        assert logger.log_interval == 500
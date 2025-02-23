import logging
import time
import pytest
from src.process_progress_logger import ProcessProgressLogger

class MockLogger:
    def __init__(self):
        self.messages = []
    
    def log(self, level, message):
        self.messages.append((level, message))

def test_init_process_progress_logger():
    """Test initialization of ProcessProgressLogger"""
    logger = ProcessProgressLogger()
    assert logger is not None

def test_log_progress_basic():
    """Test basic progress logging"""
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger, update_interval=0)
    
    logger.log_progress(5, 10)
    assert len(mock_logger.messages) == 1
    level, message = mock_logger.messages[0]
    assert level == logging.INFO
    assert "Progress: 5/10" in message
    assert "(50.00%)" in message

def test_log_progress_prefix():
    """Test custom prefix in progress logging"""
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger, update_interval=0)
    
    logger.log_progress(5, 10, prefix="Download")
    assert len(mock_logger.messages) == 1
    level, message = mock_logger.messages[0]
    assert "Download: 5/10" in message

def test_log_progress_update_interval():
    """Test logging update interval"""
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger, update_interval=0.1)
    
    logger.log_progress(1, 10)
    time.sleep(0.05)
    logger.log_progress(2, 10)
    assert len(mock_logger.messages) == 1
    
    time.sleep(0.1)
    logger.log_progress(3, 10)
    assert len(mock_logger.messages) == 2

def test_log_progress_invalid_inputs():
    """Test error handling for invalid inputs"""
    logger = ProcessProgressLogger()
    
    with pytest.raises(ValueError, match="Total must be a positive number"):
        logger.log_progress(5, 0)
    
    with pytest.raises(ValueError, match="Current progress cannot be negative"):
        logger.log_progress(-1, 10)
    
    with pytest.raises(ValueError, match="Current progress cannot exceed total"):
        logger.log_progress(11, 10)

def test_track_process():
    """Test tracking a process"""
    def mock_process(x):
        time.sleep(0.01)  # Simulate work
        return x * 2
    
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger, update_interval=0)
    
    tracked_process = logger.track_process(mock_process, total=5, prefix="Test")
    results = tracked_process(range(5))
    
    assert results == [0, 2, 4, 6, 8]
    assert len(mock_logger.messages) == 5
    
    # Check last message indicates completion
    level, message = mock_logger.messages[-1]
    assert "Test: 5/5 (100.00%)" in message
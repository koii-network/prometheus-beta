import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    """Test logger initialization."""
    logger = FrameRateLogger()
    assert logger.frame_count == 0
    assert logger.frame_rates == []
    assert logger.log_interval == 1.0

def test_frame_rate_logging():
    """Test basic frame rate logging."""
    logger = FrameRateLogger(log_interval=0.1)
    
    # Simulate frames
    time.sleep(0.2)
    frame_rate1 = logger.log_frame()
    assert frame_rate1 is not None
    assert len(logger.get_frame_rates()) == 1

def test_multiple_frame_rate_logging():
    """Test logging multiple frame rates."""
    logger = FrameRateLogger(log_interval=0.1)
    
    # Simulate multiple frames over time
    time.sleep(0.2)
    logger.log_frame()
    time.sleep(0.2)
    logger.log_frame()
    
    assert len(logger.get_frame_rates()) == 2

def test_frame_rate_reset():
    """Test resetting the frame rate logger."""
    logger = FrameRateLogger(log_interval=0.1)
    
    time.sleep(0.2)
    logger.log_frame()
    logger.reset()
    
    assert logger.frame_count == 0
    assert logger.frame_rates == []

def test_frame_logging_without_interval():
    """Test that frames are not logged before interval passes."""
    logger = FrameRateLogger(log_interval=1.0)
    
    frame_rate = logger.log_frame()
    assert frame_rate is None
    assert logger.frame_count == 1
    assert len(logger.get_frame_rates()) == 0
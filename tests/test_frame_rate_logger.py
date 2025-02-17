import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    """Test initialization of FrameRateLogger"""
    logger = FrameRateLogger()
    assert logger.frames == 0
    assert logger.start_time is None
    assert logger.log_interval == 1000
    assert logger.last_log_time is None
    assert logger.fps_callback is None

def test_start_tracking():
    """Test start_tracking method"""
    logger = FrameRateLogger()
    logger.start_tracking()
    assert logger.frames == 0
    assert logger.start_time is not None
    assert logger.last_log_time is not None

def test_log_frame_without_tracking():
    """Test log_frame when tracking hasn't started"""
    logger = FrameRateLogger()
    result = logger.log_frame()
    assert result is None

def test_log_frame_with_callback():
    """Test logging frames with a callback"""
    fps_results = []
    def mock_callback(fps):
        fps_results.append(fps)
    
    logger = FrameRateLogger(log_interval=10)  # Short interval for testing
    logger.start_tracking(fps_callback=mock_callback)
    
    # Log multiple frames quickly
    for _ in range(20):
        logger.log_frame()
        time.sleep(0.001)  # Small delay to simulate frame processing
    
    # Verify callback was called
    assert len(fps_results) > 0

def test_stop_tracking():
    """Test stop_tracking method"""
    logger = FrameRateLogger()
    logger.start_tracking()
    logger.log_frame()
    
    logger.stop_tracking()
    
    assert logger.frames == 0
    assert logger.start_time is None
    assert logger.last_log_time is None
    assert logger.fps_callback is None

def test_custom_log_interval():
    """Test custom log interval"""
    logger = FrameRateLogger(log_interval=500)  # 500ms interval
    assert logger.log_interval == 500
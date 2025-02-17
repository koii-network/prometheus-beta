import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    logger = FrameRateLogger()
    assert logger.frames_rendered == 0
    assert logger.log_interval == 1.0
    assert len(logger.frame_rate_history) == 0

def test_log_frame_single_interval():
    logger = FrameRateLogger(log_interval=0.5)
    
    # Log multiple frames
    for _ in range(10):
        logger.log_frame()
        time.sleep(0.05)  # Simulate frame rendering time
    
    # Trigger frame rate calculation
    frame_rate = logger.log_frame()
    
    assert frame_rate is not None
    assert frame_rate > 0
    assert len(logger.frame_rate_history) == 1
    
    log_entry = logger.frame_rate_history[0]
    assert 'timestamp' in log_entry
    assert 'frame_rate' in log_entry
    assert 'frames_rendered' in log_entry

def test_get_frame_rate_history():
    logger = FrameRateLogger(log_interval=0.5)
    
    # Log multiple intervals
    for _ in range(3):
        for _ in range(10):
            logger.log_frame()
            time.sleep(0.05)
        
        logger.log_frame()  # Trigger frame rate calculation
    
    history = logger.get_frame_rate_history()
    
    assert len(history) == 3
    for log_entry in history:
        assert 'timestamp' in log_entry
        assert 'frame_rate' in log_entry
        assert 'frames_rendered' in log_entry

def test_custom_log_interval():
    logger = FrameRateLogger(log_interval=2.0)
    assert logger.log_interval == 2.0
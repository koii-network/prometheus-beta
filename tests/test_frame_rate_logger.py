import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    """Test logger initialization with default and custom buffer size."""
    logger = FrameRateLogger()
    assert len(logger.frame_times) == 0
    
    logger_custom = FrameRateLogger(buffer_size=10)
    assert logger_custom.buffer_size == 10

def test_log_frame():
    """Test logging frames and buffer size management."""
    logger = FrameRateLogger(buffer_size=3)
    
    # Log multiple frames
    logger.log_frame()
    time.sleep(0.01)  # Small delay to ensure time difference
    logger.log_frame()
    time.sleep(0.01)
    logger.log_frame()
    time.sleep(0.01)
    logger.log_frame()
    
    # Check buffer maintains max size
    assert len(logger.frame_times) == 3

def test_get_fps():
    """Test FPS calculation."""
    logger = FrameRateLogger(buffer_size=5)
    
    # Not enough frames
    assert logger.get_fps() is None
    
    # Log frames with known time intervals
    start_time = time.time()
    for _ in range(5):
        logger.log_frame()
        time.sleep(0.1)  # 100ms between frames
    
    # Calculate expected FPS (should be close to 10 FPS)
    fps = logger.get_fps()
    assert fps is not None
    assert 9.5 <= fps <= 10.5

def test_reset():
    """Test resetting the frame times."""
    logger = FrameRateLogger()
    
    # Log some frames
    logger.log_frame()
    logger.log_frame()
    
    # Reset and verify empty
    logger.reset()
    assert len(logger.frame_times) == 0
    assert logger.get_fps() is None

def test_buffer_size_edge_cases():
    """Test edge cases for buffer size."""
    # Zero or negative buffer size should default to 1
    logger = FrameRateLogger(buffer_size=0)
    assert logger.buffer_size == 1
    
    # Large buffer size
    large_logger = FrameRateLogger(buffer_size=1000)
    assert large_logger.buffer_size == 1000
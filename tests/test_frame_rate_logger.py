import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    """Test logger initialization."""
    logger = FrameRateLogger()
    assert logger.sample_size == 60
    assert logger.frame_times == []
    assert logger.start_time is None

def test_frame_rate_logger_start():
    """Test start method."""
    logger = FrameRateLogger()
    logger.start()
    assert logger.frame_times == []
    assert logger.start_time is not None

def test_log_frame():
    """Test logging frames."""
    logger = FrameRateLogger(sample_size=3)
    logger.start()
    
    # Simulate frame logging with small time intervals
    time.sleep(0.01)
    frame1 = logger.log_frame()
    assert frame1 > 0
    
    time.sleep(0.02)
    frame2 = logger.log_frame()
    assert frame2 > frame1
    
    time.sleep(0.015)
    frame3 = logger.log_frame()
    assert frame3 > frame2
    
    # Check sample size limitation
    assert len(logger.frame_times) <= 3

def test_get_fps():
    """Test FPS calculation."""
    logger = FrameRateLogger(sample_size=3)
    logger.start()
    
    # No frames initially
    assert logger.get_fps() == 0.0
    
    # Log some frames with known timing
    logger.frame_times = [10, 10, 10]  # Each frame takes 10ms
    fps = logger.get_fps()
    assert abs(fps - 100.0) < 0.001  # 1000ms / 10ms per frame = 100 FPS
    
def test_get_frame_time_stats():
    """Test frame time statistics."""
    logger = FrameRateLogger(sample_size=3)
    logger.start()
    
    # Empty stats
    stats = logger.get_frame_time_stats()
    assert stats == {
        'avg_frame_time': 0.0,
        'min_frame_time': 0.0,
        'max_frame_time': 0.0
    }
    
    # With frame times
    logger.frame_times = [10, 20, 15]
    stats = logger.get_frame_time_stats()
    assert stats == {
        'avg_frame_time': 15.0,
        'min_frame_time': 10.0,
        'max_frame_time': 20.0
    }

def test_frame_rate_logger_sample_size():
    """Test sample size behavior."""
    # Test minimum sample size
    logger = FrameRateLogger(sample_size=0)
    assert logger.sample_size == 1
    
    # Test sample size limitation
    logger = FrameRateLogger(sample_size=3)
    logger.start()
    
    # Log more frames than sample size
    logger.log_frame()
    time.sleep(0.01)
    logger.log_frame()
    time.sleep(0.02)
    logger.log_frame()
    time.sleep(0.015)
    logger.log_frame()
    
    assert len(logger.frame_times) == 3  # Should not exceed sample size
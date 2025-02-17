import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    logger = FrameRateLogger()
    assert isinstance(logger, FrameRateLogger)

def test_start_logging():
    logger = FrameRateLogger()
    logger.start()
    assert logger._start_time is not None

def test_log_frame_before_start():
    logger = FrameRateLogger()
    with pytest.raises(RuntimeError, match="Frame rate logging not started"):
        logger.log_frame()

def test_get_frame_rate_before_start():
    logger = FrameRateLogger()
    with pytest.raises(RuntimeError, match="Frame rate logging not started"):
        logger.get_frame_rate()

def test_frame_rate_calculation():
    logger = FrameRateLogger()
    logger.start()
    
    # Simulate frames
    time.sleep(0.1)
    logger.log_frame()
    time.sleep(0.1)
    logger.log_frame()
    time.sleep(0.1)
    logger.log_frame()

    fps = logger.get_frame_rate()
    assert 9 <= fps <= 11  # Allow small variance due to timing

def test_frame_rate_with_duration():
    logger = FrameRateLogger()
    logger.start()
    
    # Simulate frames
    time.sleep(0.1)
    logger.log_frame()
    time.sleep(0.1)
    logger.log_frame()
    time.sleep(0.1)
    logger.log_frame()
    time.sleep(0.5)  # Wait additional time
    logger.log_frame()

    # Check FPS for last 0.3 seconds
    fps = logger.get_frame_rate(duration=0.3)
    assert 9 <= fps <= 11  # Allow small variance due to timing
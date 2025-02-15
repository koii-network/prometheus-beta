import pytest
import time
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    """Test logger initialization."""
    logger = FrameRateLogger()
    assert logger.frames_count == 0
    assert logger.log_interval == 1.0
    assert logger.on_log_callback is None

def test_frame_rate_logger_log_frame():
    """Test logging frames."""
    # Track frame rate calculation
    frame_rates = []
    def callback(frame_rate):
        frame_rates.append(frame_rate)

    logger = FrameRateLogger(log_interval=0.1)
    logger.set_log_callback(callback)

    # Log multiple frames
    for _ in range(15):
        logger.log_frame()
        time.sleep(0.01)

    # Verify callback was called
    assert len(frame_rates) > 0
    
    # Verify frame rate is within reasonable range
    for rate in frame_rates:
        assert rate > 0 and rate <= 150  # Assuming frame rates between 0-150 FPS

def test_frame_rate_logger_runtime():
    """Test total runtime tracking."""
    logger = FrameRateLogger()
    time.sleep(0.2)
    logger.log_frame()

    runtime = logger.get_total_runtime()
    assert runtime >= 0.2
    assert runtime < 0.3  # Allow some small variance

def test_frame_rate_logger_custom_interval():
    """Test logging with custom interval."""
    frame_rates = []
    def callback(frame_rate):
        frame_rates.append(frame_rate)

    logger = FrameRateLogger(log_interval=0.5)
    logger.set_log_callback(callback)

    # Log frames over a period
    for _ in range(30):
        logger.log_frame()
        time.sleep(0.02)

    # Verify at least one calculation occurred
    assert len(frame_rates) > 0